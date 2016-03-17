import bs4

import pykol.Config as Config
import pykol.Globals as Globals
from pykol.pagetypes.KoLPage import KoLPage


class Hermit(KoLPage):

    url = Config.url + 'hermit.php'

    no_worthless = "looks like you don't have anything worthless enough"

    @staticmethod
    def claim(response):
        return response.url.startswith(Hermit.url)

    @staticmethod
    def parse_page(text):
        soup = bs4.BeautifulSoup(text, 'html.parser')
        clover = soup.find('b', text='ten-leaf clover')
        clover = clover.next_element.next_element
        if 'out of stock' in clover:
            Globals.clovers = 0
        Globals.clovers = clover.text

    def auto_action(self):
        Hermit.parse_page(self.response.text)
        return None
