# -*- encoding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, InvalidPage

from aplication.news_feed.models import NewsFeedModels, FeedModels
from aplication.core.utils.url_gen import urlGen


def posts_feed_blog(request, slug):

    feed = get_object_or_404(FeedModels, slug=slug)
    news_list = NewsFeedModels.objects.filter(feed=feed)

    news_paginator = Paginator(news_list, 12)

    try:
        page = int(request.REQUEST.get('page', '1'))
    except ValueError:
        page = 1

    try:
        news = news_paginator.page(page)
    except (EmptyPage, InvalidPage):
        # If page is out of range (e.g. 9999), deliver last page of results.
        news = news_paginator.page(news_paginator.num_pages)

    url = urlGen()
    pageURI = url.generate('page', request.GET)
    items = news_list.count()

    context = {
        'title_page': 'Blog - %s' % (feed.title),
        'prefix_sub_title_page': 'Notícas',
        'sub_title_page': feed.title,
        'news_list': news,
        'total_item': items,
        'pageURI': pageURI,
        'current': page,
    }
    return render(request, 'news_feed/blog.html', context)
