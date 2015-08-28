from django.conf.urls import patterns, url

urlpatterns = patterns(
    'aplication.core.views',

    # CORE SITE
    url(r'^/?$', 'home', name='home'),
    url(r'^quem-sou-eu/?$', 'about', name='about'),
    url(r'^meus-trabalhos/?$', 'portfolio', name='portfolio'),
    url(r'^servicos/?$', 'services', name='services'),
    url(r'^contate-me/?$', 'contact', name='contact'),

    # PopUp
    url(r'^sobre\.html$', 'about_popup', name='about_popup'),
)
