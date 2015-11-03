# -*- coding: utf-8 -*-
from database_files.models import File
from aplication.news_feed.models import NewsFeedModels


def run(*args):

    for new in NewsFeedModels.objects.all():
        new.delete()
        print new

    for file in File.objects.exclude(id__in=[165, 166, 167, 168, 169]):
        file.delete()
        print file
