# -*- encoding: utf-8 -*-
from django.shortcuts import render

# Create your views here.
from .portfolio import portfolio
from .contact import contact


def home(request):
    context = {
        'title_page': 'Home'
    }
    return render(request, 'core/index.html', context)


def about(request):
    context = {
        'title_page': 'Quem Sou Eu'
    }
    return render(request, 'core/about.html', context)


def services(request):
    context = {
        'title_page': 'Meus Serviços'
    }
    return render(request, 'core/services.html', context)


def about_popup(request):
    return render(request, 'core/about_popup.html', {})
