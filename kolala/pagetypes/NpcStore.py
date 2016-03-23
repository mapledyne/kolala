import bs4

import kolala.Config as Config
import kolala.Globals as Globals
from kolala.pagetypes.KoLPage import KoLPage


class NpcStore(KoLPage):

    url = Config.url + 'shop.php'

    @staticmethod
    def claim(response):
        return response.url.startswith(NpcStore.url)

    @staticmethod
    def parse_page(text):
        soup = bs4.BeautifulSoup(text, 'html.parser')

    def auto_action(self):
        NpcStore.parse_page(self.response.text)
        return None
