# -*- encoding: utf-8 -*-
from django.shortcuts import render

# Create your views here.


def portfolio(request):
    context = {
        'title_page': 'Meu Portfólio'
    }

    context['portfolio_items'] = [
        {
            'url': '/Sites/TI_Comunicacoes',
            'image': 'http://www.cesarbruschetta.com.br/media/portfolio/site1.png',
            'title': 'TI Comunicações'
        },
        {
            'url': '/Sites/Golden_Gates',
            'image': 'http://www.cesarbruschetta.com.br/media/portfolio/site12.png',
            'title': 'Golden Gate'
        },
        {
            'url': '/Sites/Music_in_Hand/',
            'image': 'http://www.cesarbruschetta.com.br/media/portfolio/site2.png',
            'title': 'Music In Hand'
        },
        {
            'url': '/Sites/U2',
            'image': 'http://www.cesarbruschetta.com.br/media/portfolio/site3.png',
            'title': 'U2'
        },
        {
            'url': '/Sites/Cab_Inf_Old',
            'image': 'http://www.cesarbruschetta.com.br/media/portfolio/site14.png',
            'title': 'Cab Informatica - Old'
        },
        {
            'url': '/Sites/Physis',
            'image': 'http://www.cesarbruschetta.com.br/media/portfolio/site4.png',
            'title': 'Physis Jardinagem - Old'
        },
        {
            'url': '/Sites/Servicosrn_old',
            'image': 'http://www.cesarbruschetta.com.br/media/portfolio/site5.png',
            'title': 'Serviços RN - Old'
        },
        {
            'url': '/Sites/Viage_PaulaTur/',
            'image': 'http://www.cesarbruschetta.com.br/media/portfolio/site6.png',
            'title': 'Paula Tur'
        },
        {
            'url': '/Sites/Lords_of_Games/',
            'image': 'http://www.cesarbruschetta.com.br/media/portfolio/site8.png',
            'title': 'Lords Of Games'
        },
        {
            'url': '/Sites/PRB_Virtual/',
            'image': 'http://www.cesarbruschetta.com.br/media/portfolio/site7.png',
            'title': 'PRB Virtual'
        },
        {
            'url': '/Sites/Wood_Center/',
            'image': 'http://www.cesarbruschetta.com.br/media/portfolio/site9.png',
            'title': 'Wood Center'
        },
        {
            'url': '/Sites/JLS_Divisorias/',
            'image': 'http://www.cesarbruschetta.com.br/media/portfolio/site10.png',
            'title': 'JLS Divisorias - OLD'
        },
        {
            'url': '/Sites/Speedy_AM',
            'image': 'http://www.cesarbruschetta.com.br/media/portfolio/site11.png',
            'title': 'Speedy AutoMotors'
        },
        {
            'url': '/Sites/Vidal_Associados',
            'image': 'http://www.cesarbruschetta.com.br/media/portfolio/site13.png',
            'title': 'Vidal Associados'
        },
        {
            'url': '/Sites/Jogos_Flash',
            'image': 'http://www.cesarbruschetta.com.br/media/portfolio/site15.png',
            'title': 'Jogos Flash'
        },
        {
            'url': 'http://juquinhacontabel.herokuapp.com/',
            'image': 'http://www.cesarbruschetta.com.br/media/portfolio/site16.png',
            'title': 'Juquinha Contabil'
        },
        {
            'url': 'http://www.servicosrn.com.br/',
            'image': 'http://www.cesarbruschetta.com.br/media/portfolio/site5.png',
            'title': 'Serviços RN'
        },
        {
            'url': '/Sites/Xoops_Site/',
            'image': 'http://www.cesarbruschetta.com.br/media/portfolio/site18.png',
            'title': 'Xoop Media'
        },
        {
            'url': '/Sites/Elegant_Design/',
            'image': 'http://www.cesarbruschetta.com.br/media/portfolio/site19.png',
            'title': 'Elegant Design'
        },
        {
            'url': '/Sites/Cab_Inf_New',
            'image': 'http://www.cesarbruschetta.com.br/media/portfolio/site20.png',
            'title': 'Cab Informatica'
        },
        {
            'url': 'http://djangoportal.herokuapp.com/',
            'image': 'http://www.cesarbruschetta.com.br/media/portfolio/site21.png',
            'title': 'Django Portal'
        },
        {
            'url': 'http://portal-in-gae.appspot.com/',
            'image': 'http://www.cesarbruschetta.com.br/media/portfolio/site23.png',
            'title': 'Captive Green - GAE'
        },
        {
            'url': 'http://feeds-in-gae.appspot.com/',
            'image': 'http://www.cesarbruschetta.com.br/media/portfolio/site22.png',
            'title': 'Global Feeds - GAE'
        },
        {
            'url': '/Sites/King_of_Games',
            'image': 'http://www.cesarbruschetta.com.br/media/portfolio/site24.png',
            'title': 'King of Games'
        },
        {
            'url': 'http://portaldjangocms.cesarbruschetta.com.br/',
            'image': 'http://www.cesarbruschetta.com.br/media/portfolio/site25.png',
            'title': 'Django CMS'
        },
        {
            'url': 'http://django-in-gae.appspot.com/',
            'image': 'http://www.cesarbruschetta.com.br/media/portfolio/site26.png',
            'title': 'Django in GAE'
        },
        {
            'url': 'http://portal-nodejs.herokuapp.com/',
            'image': 'http://www.cesarbruschetta.com.br/media/portfolio/site27.png',
            'title': 'Portal NodeJS'
        },
    ]

    return render(request, 'core/portfolio.html', context)
