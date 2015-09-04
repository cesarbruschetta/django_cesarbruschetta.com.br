# -*- coding: utf-8 -*-
from django.template.defaultfilters import slugify
from django.core.files.temp import NamedTemporaryFile
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.db.models.loading import get_model

import feedparser
import logging
from urllib.request import urlopen

from .utils.file import FileHandler
from .rss_feed_importer import RssFeedImporter


logger = logging.getLogger(__name__)


class Parser(object):

    def __init__(self, id_feed=None, quantity=25):
        self.feed_list = self.get_feed_list(id_feed)
        self.quantity = quantity

    def parse(self):
        for feed in self.feed_list:
            logger.info("Atualizando Feed %s (%s)" % (feed['title'],
                                                      feed['url_feed'])
                        )
            self.get_content(feed['url_feed'], feed['title'], feed['id'])

    def get_feed_list(self, id_feed=None):
        """
        Metodo que busca todas as feeds no banco e retorna uma lista de
        dicionarios ordenado por ids com os feeds
        ex: [{'id': 1234, 'url_feed': 'http://foo.bar/rss/'}]
        """
        feeds = []
        FeedModels = get_model('news_feed', 'FeedModels')
        if id_feed:
            # RETORNA UMA RSS ESPECIFICADA PELO ID
            try:
                obj = FeedModels.objects.get(id=id_feed)
                feeds = [{'title': obj.title,
                          'url_feed': obj.url_feed,
                          'id': obj.id}]
            except:
                logger.info('Feed nao encontrada no banco: id=%s' % (id_feed))
                pass
        else:
            # RETORNA TODAS AS RSS ATIVAS NO BANCO DE DADOS
            feeds = FeedModels.objects\
                .filter(status=FeedModels.ACTIVE)\
                .values('url_feed', 'title', 'id')

        return feeds

    def get_content(self, url, feed_title, feed_id):
        NewsFeedModels = get_model('news_feed', 'NewsFeedModels')

        i = 0
        feeds = feedparser.parse(url)
        for feed in feeds.entries:
            # se iteramos até o limite informado, quebramos o loop
            if i == self.quantity:
                break

            item = RssFeedImporter(feed)
            slug = slugify(item.title)

            # já existe no banco? se sim passo para a proxima iteracao
            try:
                news = NewsFeedModels.objects.get(slug=slug)
            except NewsFeedModels.DoesNotExist:
                news = NewsFeedModels()

            news.feed_id = feed_id
            news.title = item.title
            news.slug = slug
            news.content = item.content
            news.description = item.description
            news.created = item.date
            news.link = item.link
            # news.category = simplejson.dumps(item.category)

            if item.img:
                try:
                    image_response = urlopen(item.img)
                    # image_content.write(urlopen(item.img).read())
                # Existem muitas excessoes que podem estourar
                except:
                    image_response = None
                    pass

                if image_response:
                    image_temp = NamedTemporaryFile(delete=True)
                    image_content = image_response.read()
                    image_name = FileHandler\
                        .generate_filename_based_on_url(item.img)

                    image_temp.write(image_content)
                    image_size = len(image_content)
                    http_message = image_response.info()
                    content_type = http_message.get_content_type()
                    image_file = InMemoryUploadedFile(
                        file=image_temp,
                        name=image_name,
                        field_name='imagem',
                        content_type=content_type,
                        size=image_size,
                        charset=None
                    )
                    image_temp.flush()
                    image_temp.seek(0)
                    news.imagem.save(image_name, image_file, save=True)

            news.save()

            # contador para a quantidade limite imposta
            i = i + 1
