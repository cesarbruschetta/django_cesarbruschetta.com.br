from django.conf.urls import patterns, url

urlpatterns = patterns(
    'aplication.core.views',

    # AJAX
    url(r'^/?$', 'home', name='home'),
    url(r'^quem-sou-eu/?$', 'about', name='about'),


)
