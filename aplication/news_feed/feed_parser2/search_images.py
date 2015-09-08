# -*- coding: utf-8 -*-
from django.conf import settings
from django.core.cache import get_cache
from django.template.defaultfilters import slugify

from google import google, images


class SearchImagens(object):

    '''
        Mecanismo que buscar os resultado de imagem no Google

        https://github.com/abenassi/Google-Search-AP
    '''

    options = images.ImageOptions()
    options.size_category = images.SizeCategory.MEDIUM
    options.larger_than = images.LargerThan.VGA
    options.color_type = images.ColorType.COLOR

    def __init__(self, query):
        self.query = query

    def result(self):
        return self.cache()

    def search(self):
        # results = google.search_images(self.query,
        #                                self.options)
        results = []
        if len(results):
            item = results[0]
            return item.link
        else:
            return '%score/images/placeholdi_news.png' % (settings.STATIC_URL)

    def cache(self):

        cache = get_cache('default')
        strip_query = slugify(self.query)
        key = 'searchimagens:{0}'.format(strip_query)

        cached_data = cache.get(key)
        if cached_data:
            return cached_data
        else:
            result = self.search()

            timeout = 60 * 60 * 24
            cache.set(key, result, timeout)

            return result
