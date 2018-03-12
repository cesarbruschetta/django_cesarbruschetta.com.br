# -*- encoding: utf-8 -*-
from django.shortcuts import render

# Create your views here.


def portfolio(request):
    context = {
        'title_page': 'Meu Portfólio'
    }

    context['portfolio_items'] = [
        {
            'url': 'http://sites.cesarbruschetta.com.br/TI_Comunicacoes',
            'image': '/static/core/portfolio/site1.png',
            'title': 'TI Comunicações'
        },
        {
            'url': 'http://sites.cesarbruschetta.com.br/Golden_Gates',
            'image': '/static/core/portfolio/site12.png',
            'title': 'Golden Gate'
        },
        {
            'url': 'http://sites.cesarbruschetta.com.br/Music_in_Hand/',
            'image': '/static/core/portfolio/site2.png',
            'title': 'Music In Hand'
        },
        {
            'url': 'http://sites.cesarbruschetta.com.br/U2',
            'image': '/static/core/portfolio/site3.png',
            'title': 'U2'
        },
        {
            'url': 'http://sites.cesarbruschetta.com.br/Cab_Inf_Old',
            'image': '/static/core/portfolio/site14.png',
            'title': 'Cab Informatica - Old'
        },
        {
            'url': 'http://sites.cesarbruschetta.com.br/Physis',
            'image': '/static/core/portfolio/site4.png',
            'title': 'Physis Jardinagem - Old'
        },
        {
            'url': 'http://sites.cesarbruschetta.com.br/Servicosrn_old',
            'image': '/static/core/portfolio/site5.png',
            'title': 'ServiÃ§os RN - Old'
        },
        {
            'url': 'http://sites.cesarbruschetta.com.br/Viage_PaulaTur/',
            'image': '/static/core/portfolio/site6.png',
            'title': 'Paula Tur'
        },
        {
            'url': 'http://sites.cesarbruschetta.com.br/Lords_of_Games/',
            'image': '/static/core/portfolio/site8.png',
            'title': 'Lords Of Games'
        },
        {
            'url': 'http://sites.cesarbruschetta.com.br/PRB_Virtual/',
            'image': '/static/core/portfolio/site7.png',
            'title': 'PRB Virtual'
        },
        {
            'url': 'http://sites.cesarbruschetta.com.br/Wood_Center/',
            'image': '/static/core/portfolio/site9.png',
            'title': 'Wood Center'
        },
        {
            'url': 'http://sites.cesarbruschetta.com.br/JLS_Divisorias/',
            'image': '/static/core/portfolio/site10.png',
            'title': 'JLS Divisorias - Old'
        },
        {
            'url': 'http://sites.cesarbruschetta.com.br/Speedy_AM',
            'image': '/static/core/portfolio/site11.png',
            'title': 'Speedy AutoMotors'
        },
        {
            'url': 'http://sites.cesarbruschetta.com.br/Vidal_Associados',
            'image': '/static/core/portfolio/site13.png',
            'title': 'Vidal Associados'
        },
        {
            'url': 'http://sites.cesarbruschetta.com.br/Jogos_Flash',
            'image': '/static/core/portfolio/site15.png',
            'title': 'Jogos Flash'
        },
        {
            'url': 'http://juquinhacontabel.herokuapp.com/',
            'image': '/static/core/portfolio/site16.png',
            'title': 'Juquinha Contabil'
        },
        {
            'url': 'http://www.servicosrn.com.br/',
            'image': '/static/core/portfolio/site5.png',
            'title': 'Serviços RN'
        },
        {
            'url': 'http://sites.cesarbruschetta.com.br/Xoops_Site/',
            'image': '/static/core/portfolio/site18.png',
            'title': 'Xoop Media'
        },
        {
            'url': 'http://sites.cesarbruschetta.com.br/Elegant_Design/',
            'image': '/static/core/portfolio/site19.png',
            'title': 'Elegant Design'
        },
        {
            'url': 'http://sites.cesarbruschetta.com.br/Cab_Inf_New',
            'image': '/static/core/portfolio/site20.png',
            'title': 'Cab Informatica'
        },
        {
            'url': 'http://djangoportal.herokuapp.com/',
            'image': '/static/core/portfolio/site21.png',
            'title': 'Django Portal'
        },
        {
            'url': 'http://portal-in-gae.appspot.com/',
            'image': '/static/core/portfolio/site23.png',
            'title': 'Captive Green - GAE'
        },
        {
            'url': 'http://feeds-in-gae.appspot.com/',
            'image': '/static/core/portfolio/site22.png',
            'title': 'Global Feeds - GAE'
        },
        {
            'url': 'http://sites.cesarbruschetta.com.br/King_of_Games',
            'image': '/static/core/portfolio/site24.png',
            'title': 'King of Games'
        },
        {
            'url': 'http://portaldjangocms.herokuapp.com/',
            'image': '/static/core/portfolio/site25.png',
            'title': 'Django CMS'
        },
        {
            'url': 'http://django-in-gae.appspot.com/',
            'image': '/static/core/portfolio/site26.png',
            'title': 'Django in GAE'
        },
        {
            'url': 'http://portal-nodejs.herokuapp.com/',
            'image': '/static/core/portfolio/site27.png',
            'title': 'Portal NodeJS'
        },
        {
            'url': 'http://cab.cesarbruschetta.com.br/',
            'image': '/static/core/portfolio/site28.png',
            'title': u'Cab Informática'
        },
        {
            'url': 'http://plone.cesarbruschetta.com.br/',
            'image': '/static/core/portfolio/site29.png',
            'title': 'Cesar Augusto - Old'
        },
    ]

    return render(request, 'core/portfolio.html', context)
