# -*- encoding: utf-8 -*-

from django.db import models
from django.template.defaultfilters import slugify


class FeedModels(models.Model):

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
    description = models.TextField(verbose_name=u'Descrição', default='')
    status = models.PositiveSmallIntegerField(choices=STATUS,
                                              default=ACTIVE)


class NewsFeedModels(models.Model):

    feed = models.ForeignKey('news_feed.FeedModels')
    title = models.CharField(verbose_name="Titulo",
                             default="", max_length=255)
    slug = models.SlugField(default='', blank=True, null=True)
    content = models.TextField(verbose_name=u'Conteudo', default='')
    created = models.DateTimeField(auto_now=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(NewsFeedModels, self).save(*args, **kwargs)

    def __unicode__(self):
        return '%s : %s - %s' % (self.feed.title, self.title,
                                 self.created.strftime('%d/%m/%Y %H:%M'))
