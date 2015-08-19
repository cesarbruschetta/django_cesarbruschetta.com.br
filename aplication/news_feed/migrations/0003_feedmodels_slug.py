# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news_feed', '0002_auto_20150818_1715'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedmodels',
            name='slug',
            field=models.SlugField(max_length=255, unique=True, default=''),
        ),
    ]
