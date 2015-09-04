# -*- encoding: utf-8 -*-
from django.shortcuts import render


from aplication.news_feed.models import NewsFeedModels


def home(request):

    news_list = NewsFeedModels.objects.all()
    news_list = news_list.exclude(imagem='')

    context = {
        'title_page': 'Home',
        'highlights_list': news_list[:4],
    }
    return render(request, 'core/index.html', context)
