# -*- encoding: utf-8 -*-
from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from aplication.news_feed.models import NewsFeedModels

# Create your views here.


def blog_home(request):

    news_list = NewsFeedModels.objects.all()
    news_paginator = Paginator(news_list, 10)

    page = request.REQUEST.get('page', '1')
    try:
        news = news_paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        news = news_paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        news = news_paginator.page(news_paginator.num_pages)

    context = {
        'title_page': 'Blog',
        'news': news
    }
    return render(request, 'news_feed/blog.html', context)


def post_blog(request, slug):
    context = {
        'title_page': 'Home'
    }
    return render(request, 'news_feed/single.html', context)
