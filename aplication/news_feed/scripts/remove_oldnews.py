# -*- coding: utf-8 -*-

from aplication.news_feed.models import NewsFeedModels

from datetime import datetime, timedelta

import logging
logger = logging.getLogger(__name__)


def run(*args):

    now = datetime.now()
    last_month = now - timedelta(days=30)

    logger.info(
        'Removendo Noticias ate %s' % (last_month.strftime('%d/%m/%Y'))
    )
    old_news = NewsFeedModels.objects.filter(created__gte=last_month)
    count_itens = old_news.count()
    for news in old_news:
        news.delete()

    logger.info('Foram Removidas %s itens' % (count_itens))
