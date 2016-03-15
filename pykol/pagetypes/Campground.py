import bs4

import pykol
from pykol.pagetypes.KoLPage import KoLPage


class Campground(KoLPage):

    url = pykol.Config.url + 'campground.php'

    @staticmethod
    def claim(response):
        return response.url.startswith(Campground.url)

    @staticmethod
    def parse_page(text):
        soup = bs4.BeautifulSoup(text, 'html.parser')
        home = soup.find('a', href='campground.php?action=rest')
        home = home.img['alt'].replace(' (1)', '').replace('Rest in Your ', '')
        pykol.player.home = home

        witchess = soup('a', href='campground.php?action=witchess')
        if witchess is not None:
            pykol.player.witchess = True

    def auto_action(self):
        Campground.parse_page(self.response.text)
        return None
