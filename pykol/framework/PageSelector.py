import pykol.Config as Config
from pykol.framework.Logging import Logging
from pykol.pagetypes import *  # noqa


class PageSelector(object):

    def __init__(self, response):
        self.response = response

    def page(self):
        page_name = self.response.url.replace(Config.url, '').split('?')[0]
        if Config.save_pages:
            with open(Config.save_pages_path +
                      page_name,
                      'w+') as file:
                file.write(self.response.text.encode('utf-8'))

        for page in KoLPage.__subclasses__():
            if page.claim(self.response):
                Logging.debug('Page claimed by: ' + page.__name__)
                return page(self.response)
        Logging.info('### Page ({}) went unclaimed.'.format(page_name))
        return KoLPage(self.response)
