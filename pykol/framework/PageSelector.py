import bs4
import pykol.Config as Config
import pykol.pagetypes as pagetypes


class PageSelector(object):

    def __init__(self, response):
        self.soup = bs4.BeautifulSoup(response.text)
        self.response = response

    def page(self):
        with open('_pages/' + self.response.url.replace(Config.url, '').split('?')[0], 'w+') as file:
            file.write(self.response.text.encode('utf-8'))

        for page in pagetypes.KoLPage.__subclasses__():
            if page.claim(self.response):
                return page(self.response)
        return pagetypes.KoLPage(self.response)
