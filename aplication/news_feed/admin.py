from django.contrib import admin

from aplication.news_feed.models import FeedModels, NewsFeedModels

# Register your models here.
admin.site.register(FeedModels)
admin.site.register(NewsFeedModels)
