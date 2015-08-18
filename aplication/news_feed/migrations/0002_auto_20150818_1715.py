# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news_feed', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedmodels',
            name='logo',
            field=models.ImageField(default='', upload_to=''),
        ),
        migrations.AlterField(
            model_name='feedmodels',
            name='description',
            field=models.TextField(blank=True, verbose_name='Descrição', null=True),
        ),
    ]
