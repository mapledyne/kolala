import pykol.Config as Config
import pykol.pagetypes as pagetypes


class PageSelector(object):

    def __init__(self, response):
        self.response = response

    def page(self):
        if Config.save_pages:
            with open(Config.save_pages_path +
                      self.response.url.replace(Config.url, '').split('?')[0],
                      'w+') as file:
                file.write(self.response.text.encode('utf-8'))

        for page in pagetypes.KoLPage.__subclasses__():
            if page.claim(self.response):
                return page(self.response)
        return pagetypes.KoLPage(self.response)
