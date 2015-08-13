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
            'image': 'http://cab.cesarbruschetta.com.br/banco-de-imagens/site1.png/image_thumb',
            'title': 'TI Comunicações'
        },
        {
            'url': '/Sites/Golden_Gates',
            'image': 'http://cab.cesarbruschetta.com.br/banco-de-imagens/site12.png/image_thumb',
            'title': 'Golden Gate'
        },
        {
            'url': '/Sites/Music_in_Hand/',
            'image': 'http://cab.cesarbruschetta.com.br/banco-de-imagens/site2.png/image_thumb',
            'title': 'Music In Hand'
        },
        {
            'url': '/Sites/U2',
            'image': 'http://cab.cesarbruschetta.com.br/banco-de-imagens/site3.png/image_thumb',
            'title': 'U2'
        },
        {
            'url': '/Sites/Cab_Inf_Old',
            'image': 'http://cab.cesarbruschetta.com.br/banco-de-imagens/site14.png/image_thumb',
            'title': 'Cab Informatica - Old'
        },
        {
            'url': '/Sites/Physis',
            'image': 'http://cab.cesarbruschetta.com.br/banco-de-imagens/site4.png/image_thumb',
            'title': 'Physis Jardinagem - Old'
        },
        {
            'url': '/Sites/Servicosrn_old',
            'image': 'http://cab.cesarbruschetta.com.br/banco-de-imagens/site5.png/image_thumb',
            'title': 'Serviços RN - Old'
        },
        {
            'url': '/Sites/Viage_PaulaTur/',
            'image': 'http://cab.cesarbruschetta.com.br/banco-de-imagens/site6.png/image_thumb',
            'title': 'Paula Tur'
        },
        {
            'url': '/Sites/Lords_of_Games/',
            'image': 'http://cab.cesarbruschetta.com.br/banco-de-imagens/site8.png/image_thumb',
            'title': 'Lords Of Games'
        },
        {
            'url': '/Sites/PRB_Virtual/',
            'image': 'http://cab.cesarbruschetta.com.br/banco-de-imagens/site7.png/image_thumb',
            'title': 'PRB Virtual'
        },
        {
            'url': '/Sites/Wood_Center/',
            'image': 'http://cab.cesarbruschetta.com.br/banco-de-imagens/site9.png/image_thumb',
            'title': 'Wood Center'
        },
        {
            'url': '/Sites/JLS_Divisorias/',
            'image': 'http://cab.cesarbruschetta.com.br/banco-de-imagens/site10.png/image_thumb',
            'title': 'JLS Divisorias - OLD'
        },
        {
            'url': '/Sites/Speedy_AM',
            'image': 'http://cab.cesarbruschetta.com.br/banco-de-imagens/site11.png/image_thumb',
            'title': 'Speedy AutoMotors'
        },
        {
            'url': '/Sites/Vidal_Associados',
            'image': 'http://cab.cesarbruschetta.com.br/banco-de-imagens/site13.png/image_thumb',
            'title': 'Vidal Associados'
        },
        {
            'url': '/Sites/Jogos_Flash',
            'image': 'http://cab.cesarbruschetta.com.br/banco-de-imagens/site15.png/image_thumb1',
            'title': 'Jogos Flash'
        },
        {
            'url': 'http://juquinhacontabel.herokuapp.com/',
            'image': 'http://cab.cesarbruschetta.com.br/banco-de-imagens/site16.png/image_thumb',
            'title': 'Juquinha Contabil'
        },
        {
            'url': 'http://www.servicosrn.com.br/',
            'image': 'http://cab.cesarbruschetta.com.br/banco-de-imagens/site5.png/image_thumb',
            'title': 'Serviços RN'
        },
        {
            'url': '/Sites/Xoops_Site/',
            'image': 'http://cab.cesarbruschetta.com.br/banco-de-imagens/site18.png/image_thumb',
            'title': 'Xoop Media'
        },
        {
            'url': '/Sites/Elegant_Design/',
            'image': 'http://cab.cesarbruschetta.com.br/banco-de-imagens/site19.png/image_thumb',
            'title': 'Elegant Design'
        },
        {
            'url': '/Sites/Cab_Inf_New',
            'image': 'http://cab.cesarbruschetta.com.br/banco-de-imagens/site20.png/image_thumb',
            'title': 'Cab Informatica'
        },
        {
            'url': 'http://djangoportal.herokuapp.com/',
            'image': 'http://cab.cesarbruschetta.com.br/banco-de-imagens/site21.png/image_mini',
            'title': 'Django Portal'
        },
        {
            'url': 'http://portal-in-gae.appspot.com/',
            'image': 'http://cab.cesarbruschetta.com.br/banco-de-imagens/site23.png/image_thumb',
            'title': 'Captive Green - GAE'
        },
        {
            'url': 'http://feeds-in-gae.appspot.com/',
            'image': 'http://cab.cesarbruschetta.com.br/banco-de-imagens/site22.png/image_thumb',
            'title': 'Global Feeds - GAE'
        },
        {
            'url': '/Sites/King_of_Games',
            'image': 'http://cab.cesarbruschetta.com.br/banco-de-imagens/site24.png/image_mini',
            'title': 'King of Games'
        },
        {
            'url': 'http://portaldjangocms.cesarbruschetta.com.br/',
            'image': 'http://cab.cesarbruschetta.com.br/banco-de-imagens/site25.jpeg/image_mini',
            'title': 'Django CMS'
        },
        {
            'url': 'http://django-in-gae.appspot.com/',
            'image': 'http://cab.cesarbruschetta.com.br/banco-de-imagens/site26.png/image_thumb',
            'title': 'Django in GAE'
        },
        {
            'url': 'http://portal-nodejs.herokuapp.com/',
            'image': 'http://cab.cesarbruschetta.com.br/banco-de-imagens/site27.png/image_thumb',
            'title': 'Portal NodeJS'
        },
    ]

    return render(request, 'portfolio.html', context)
