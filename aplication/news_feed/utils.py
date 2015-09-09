# -*- encoding: utf-8 -*-

from itertools import zip_longest


def grouper(iterable, n, fillvalue=None):
    "Collect data into fixed-length chunks or blocks"
    # grouper('ABCDEFG', 3, 'x') --> ABC DEF Gxx
    args = [iter(iterable)] * n
    return list(zip_longest(fillvalue=fillvalue, *args))


def split_news(resultset_news):
    result = []
    not_image = resultset_news.filter(imagem='')
    wich_image = resultset_news.exclude(imagem='')

    grup_not_image = grouper(not_image, 12)
    grup_wich_image = grouper(wich_image, 12)
    max_itens = max((len(grup_not_image), len(grup_wich_image)))

    for i in range(max_itens):

        try:
            result += grup_wich_image[i]
        except:
            pass

        try:
            result += grup_not_image[i]
        except:
            pass

    return result
