# -*- coding: utf-8 -*-

from datetime import datetime
from bs4 import BeautifulSoup
from html.parser import HTMLParser


from .utils.html import strip_tags
from .utils.datetime import parse_str2datetime


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
            content = self.feed['content']['value']
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
        # tags = self.feed.get('tags', None)
        # if tags:
        #     tags = [tag['term'] for tag in tags]

        # return tags
        return ''

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
                src = None

        if not src:
            # buscamos a primeira tag de img no content
            try:
                img_tag = BeautifulSoup(HTMLParser()
                                        .unescape(self.content)
                                        ).first('img')
            except:
                img_tag = None

            if img_tag:
                # @todo: se for uma img estranha do feedburner tratar!yy
                src = dict(img_tag.attrs).get('src', None)

        return src

    @property
    def has_content(self):
        # se gerar um KeyError eu sei que não existe, não achei outra forma
        try:
            self.feed['content_detail']['value']
            to_return = True
        except KeyError:
            to_return = False

        return to_return

    @property
    def date(self):

        try:
            str_date = self.feed.published_parsed
        except AttributeError:
            str_date = self.feed.updated_parsed

        try:
            return parse_str2datetime(str_date)
        except:
            return datetime.now()
