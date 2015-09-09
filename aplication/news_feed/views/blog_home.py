# -*- encoding: utf-8 -*-
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, InvalidPage

from aplication.core.utils.url_gen import urlGen
from aplication.news_feed.models import NewsFeedModels
from aplication.news_feed.utils import split_news


def blog_home(request):

    news_list = NewsFeedModels.objects.all()

    # DIVIDE  A LISTA DE NEWS EM COM E SEM IMAGEM
    news_list = split_news(news_list)
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
    items = len(news_list)

    context = {
        'title_page': 'Blog',
        'prefix_sub_title_page': 'Últimas',
        'sub_title_page': 'Notícias',
        'news_list': news,
        'total_item': items,
        'pageURI': pageURI,
        'current': page,
    }
    return render(request, 'news_feed/blog.html', context)
