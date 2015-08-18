# -*- coding: utf-8 -*-

from aplication.news_feed.feed_parser2 import Parser


import logging
logger = logging.getLogger(__name__)


def run(*args):

    p = Parser()
    p.parse()

    logger.info('Feed Atualizado com sucesso')
