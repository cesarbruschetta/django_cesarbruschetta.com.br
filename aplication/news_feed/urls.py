from django.conf.urls import patterns, url

urlpatterns = patterns(
    'aplication.news_feed.views',

    # AJAX
    url(r'^/?$', 'blog_home', name='blog_home'),


)
