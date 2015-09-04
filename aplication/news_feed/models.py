# -*- encoding: utf-8 -*-

from django.db import models
from django.template.defaultfilters import slugify

from datetime import datetime
import re

from aplication.core.utils.models import *
from aplication.news_feed.feed_parser2 import SearchImagens


class FeedModels(models.Model):

    class Meta:
        verbose_name = u'Feed RSS'
        verbose_name_plural = u'Feeds RSS'
        ordering = ('title',)

    ACTIVE = 1
    INACTIVE = 0

    STATUS = (
        (ACTIVE, u'Ativo'),
        (INACTIVE, u'Inativo'),
    )

    url_feed = models.CharField(verbose_name="URL do feed",
                                default="", max_length=255)

    title = models.CharField(verbose_name="Titulo",
                             default="", max_length=255)
    description = models.TextField(verbose_name=u'Descrição', **NULL)
    logo = models.ImageField(upload_to='', default='')
    slug = models.SlugField(default='', unique=True, max_length=255)
    status = models.PositiveSmallIntegerField(choices=STATUS,
                                              default=ACTIVE)

    def __str__(self):
        return '%s - %s' % (self.title, self.url_feed)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(FeedModels, self).save(*args, **kwargs)


class NewsFeedModels(models.Model):

    u'''
        Modelo que representa uma noticia, a mesma está vinculada a um rss
    '''
    class Meta:
        verbose_name = u'Notícia'
        verbose_name_plural = u'Notícias'
        ordering = ('-created',)

    feed = models.ForeignKey('news_feed.FeedModels')
    title = models.CharField(verbose_name="Titulo", **CHARN)
    description = models.TextField(u"Subtítulo da notícia", default='')
    content = models.TextField(verbose_name=u'Conteudo', default='')

    category = models.CharField(**CHARN)
    slug = models.SlugField(default='', unique=True, max_length=255)
    link = models.CharField(**CHARN)
    imagem = models.ImageField(upload_to='', **NULL)

    created = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return '%s : %s - %s' % (self.feed.title, self.title,
                                 self.created.strftime('%d/%m/%Y %H:%M'))

    def get_content(self):
        p = re.compile(r'<img .*?>')
        return p.sub('', self.content)

    def get_imagem(self):
        if self.imagem:
            return self.imagem.url
        else:
            search = SearchImagens(self.title)

            return search.result()
