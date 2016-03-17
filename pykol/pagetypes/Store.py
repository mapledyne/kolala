import bs4

import pykol.Config as Config
import pykol.Globals as Globals
from pykol.pagetypes.KoLPage import KoLPage


class Store(KoLPage):

    url = Config.url + 'store.php'

    @staticmethod
    def claim(response):
        return response.url.startswith(Store.url)

    @staticmethod
    def parse_page(text):
        soup = bs4.BeautifulSoup(text, 'html.parser')

    def auto_action(self):
        Store.parse_page(self.response.text)
        return None
