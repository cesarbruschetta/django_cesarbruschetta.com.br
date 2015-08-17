# -*- coding: utf-8 -*-

import feedparser
from hashlib import md5
from datetime import datetime
from urllib2 import urlopen

from django.utils import simplejson, timezone
from django.template.defaultfilters import slugify

from django.core.files.temp import NamedTemporaryFile
from django.core.files.uploadedfile import InMemoryUploadedFile


from aplication.core.models import NewsFeedModels, FeedModels


from .utils.file import FileHandler
from .rss_feed_importer import RssFeedImporter

import logging
logger = logging.getLogger(__name__)


class Parser(object):

    def __init__(self, id_feed=None, quantity=25):
        self.feed_list = self.get_feed_list(id_feed)
        self.quantity = quantity

    def get_feed_list(self, id_feed=None):
        """
        Metodo que busca todas as feeds no banco e retorna uma lista de
        dicionarios ordenado por ids com os feeds
        ex: [{'id': 1234, 'url_feed': 'http://foo.bar/rss/'}]
        """
        feeds = []
        if id_feed:
            # RETORNA UMA RSS ESPECIFICADA PELO ID
            try:
                obj = FeedModels.objects.get(id=id_feed)
                feeds = [{'title': obj.title, 'url_feed': obj.url_feed}]
            except:
                logger.info('Feed nao encontrada no banco: id=%s' % (id_feed))
                pass
        else:
            # RETORNA TODAS AS RSS ATIVAS NO BANCO DE DADOS
            feeds = FeedModels.objects\
                .filter(status=FeedModels.ACTIVE)\
                .values('url_feed', 'title')

        return feeds

    def get_content(self, url, title_rss):
        print title_rss
        print url

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

            news.titulo = item.title
            news.slug = slug

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

                    image_name = md5(image_name).hexdigest()
                    image_temp.write(image_content)
                    image_size = len(image_content)
                    http_message = image_response.info()
                    content_type = http_message.type
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

            news.content = item.content
            news.description = item.description
            try:
                news.created = item.date.replace(tzinfo=timezone.utc)
            except:
                news.created = datetime.utcnow().replace(tzinfo=timezone.utc)
            news.link = item.link
            news.category = simplejson.dumps(item.category)
            news.save()

            # contador para a quantidade limite imposta
            i = i + 1

    def parse(self):
        for feed in self.feed_list:
            self.get_content(feed['url_feed'], feed['title'])
