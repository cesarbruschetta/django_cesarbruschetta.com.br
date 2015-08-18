# -*- coding: utf-8 -*-
from urllib.parse import urlparse


class FileHandler(object):

    """Simple helper class to work with files"""

    def __init__(self):
        super(FileHandler, self).__init__()

    @staticmethod
    def generate_filename_based_on_url(url):
        '''
        gera um filename a partir da url passada
        '''
        parsed_url = urlparse(url)
        fileinfo = parsed_url.path.split('/')[-1].split('.')
        # retorno o filename completo
        try:
            filename = fileinfo[0] + '.' + fileinfo[1]
        except IndexError:
            filename = 'random'

        return filename
