# -*- coding: utf-8 -*-

import os
from codecs import open as c_open

from django.conf import settings
from django.template import loader
from django.utils.html import escape
from django.utils.safestring import mark_safe
from bs4 import BeautifulSoup, Comment
from html.parser import HTMLParser


def render_to_file(filename, template, context, path='rendered'):
    render_path = os.path.join(settings.MEDIA_ROOT, '%s/%s' % (path, filename))
    f = c_open(render_path, "w", encoding="utf-8")
    conteudo = loader.render_to_string(template, context)
    f.write(conteudo)
    f.close()


# @see: http://djangosnippets.org/snippets/2002/
def strip_tags(text, valid_tags={}):
    """
    Recebe uma string html e uma lista de tag e atributos validos
    Exemplo:
    '<li><a href='#' title='bar' style=''>link</a></li>', {'a': 'href title'}

    retorna: <a href='#' title='bar'>link</a>
    """
    try:
        text = HTMLParser().unescape(text)
        soup = BeautifulSoup(text)
        for comment in soup.findAll(text=lambda text: isinstance(text, Comment)):
            comment.extract()
        for tag in soup.findAll(True):
            if tag.name in valid_tags:
                valid_attrs = valid_tags[tag.name]
                # tag.attrs = [(attr, val.replace('javascript:', ''))
                #              for attr, val in tag.attrs if attr in valid_attrs]

                attrs = {}
                for attr, val in tag.attrs.items():
                    if attr in valid_attrs:
                        attrs[attr] = val.replace('javascript:', '')

                tag.attrs = attrs

            else:
                tag.hidden = True
        return soup.renderContents().decode('utf8')
    except Exception as ex:
        return str(ex)



def htmlentities(s):
    return mark_safe(escape(s).encode('ascii', 'xmlcharrefreplace'))


def string_to_bool(string):
    u"""
        Método que recebe uma string TRUE, true, True, 1 ou 0 False, false
        FALSE e retorna um booleano
    """
    # if type(string) == bool:
    #     return string

    string = str(string)
    string = string.lower()
    if string == 'true' or string == "1":
        return True
    else:
        return False
