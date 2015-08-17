# -*- coding: utf-8 -*-

from datetime import datetime
from time import mktime
from BeautifulSoup import BeautifulSoup
from HTMLParser import HTMLParser

from .utils.html import strip_tags

import sys


class RssFeedImporter(object):

    """
        Classe abstrata que define todos os metodos
        comuns a todos os rss do banco
    """
    ALLOWED_HTML_TAGS = {'p': '',
                         'strong': '',
                         'span': '',
                         'em': '',
                         'img': 'src'}

    ALLOWED_IMAGES = ['image/jpeg', 'image/jpg', 'image/png', 'image/gif']

    BLOCKED_URL = ['feedburner']

    def __init__(self, feed):
        self.feed = feed

    @property
    def content(self):
        if self.has_content:
            content = self.feed['content'][0]['value']
        else:
            content = self.feed.get('summary', None)

        return strip_tags(content, self.ALLOWED_HTML_TAGS)

    @property
    def title(self):
        return self.feed.get('title', None)

    @property
    def description(self):
        description = self.feed.get('summary', None)
        if not description or not self.has_content:
            description = ""

        return strip_tags(description, self.ALLOWED_HTML_TAGS)

    @property
    def link(self):
        return self.feed.get('link', None)

    @property
    def category(self):
        tags = self.feed.get('tags', None)
        if tags:
            tags = [tag['term'] for tag in tags]

        return tags

    @property
    def img(self):
        # pegamos todas, porém só uso a primeira, sempre
        imgs = self.feed.get('links', None)
        src = None
        if imgs:
            src = [l['href'] for l in imgs if l['type'] in self.ALLOWED_IMAGES]
            if src:
                src = src[0]
            else:
                # buscamos a primeira tag de img no content
                img_tag = BeautifulSoup(self.content).first('img')
                if img_tag:
                    # @todo: se for uma img estranha do feedburner tratar!yy
                    src = dict(img_tag.attrs).get('src', None)
        else:
            img_tag = BeautifulSoup(HTMLParser()
                                    .unescape(self.content)
                                    ).first('img')
            if img_tag:
                # @todo: se for uma img estranha do feedburner tratar!yy
                src = dict(img_tag.attrs).get('src', None)
        return src

    @property
    def has_content(self):
        # se gerar um KeyError eu sei que não existe, não achei outra forma
        try:
            self.feed['content'][0]['value']
            to_return = True
        except KeyError:
            to_return = False

        return to_return

    @property
    def date(self):
        try:
            date = self.feed.published_parsed
        except AttributeError:
            date = self.feed.updated_parsed

        return datetime.fromtimestamp(mktime(date))
