# -*- encoding: utf-8 -*-
from django.shortcuts import render

# Create your views here.


def home(request):
    context = {
        'title_page': 'Home'
    }
    return render(request, 'index.html', context)


def about(request):
    context = {
        'title_page': 'Quem Sou Eu'
    }
    return render(request, 'about.html', context)
