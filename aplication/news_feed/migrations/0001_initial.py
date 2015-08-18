# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FeedModels',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('url_feed', models.CharField(verbose_name='URL do feed', max_length=255, default='')),
                ('title', models.CharField(verbose_name='Titulo', max_length=255, default='')),
                ('description', models.TextField(verbose_name='Descrição', default='')),
                ('status', models.PositiveSmallIntegerField(choices=[(1, 'Ativo'), (0, 'Inativo')], default=1)),
            ],
            options={
                'verbose_name': 'Feed RSS',
                'verbose_name_plural': 'Feeds RSS',
                'ordering': ('title',),
            },
        ),
        migrations.CreateModel(
            name='NewsFeedModels',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('title', models.CharField(verbose_name='Titulo', max_length=255, blank=True, null=True)),
                ('description', models.TextField(verbose_name='Subtítulo da notícia', default='')),
                ('content', models.TextField(verbose_name='Conteudo', default='')),
                ('category', models.CharField(max_length=255, blank=True, null=True)),
                ('slug', models.SlugField(max_length=255, unique=True, default='')),
                ('link', models.CharField(max_length=255, blank=True, null=True)),
                ('imagem', models.ImageField(upload_to='', blank=True, null=True)),
                ('created', models.DateTimeField(default=datetime.datetime.now)),
                ('feed', models.ForeignKey(to='news_feed.FeedModels')),
            ],
            options={
                'verbose_name': 'Notícia',
                'verbose_name_plural': 'Notícias',
                'ordering': ('-created',),
            },
        ),
    ]
