import bs4

import kolala
import kolala.Globals
from kolala.pagetypes.KoLPage import KoLPage


class TopMenu(KoLPage):

    url = kolala.Globals.url + 'awesomemenu.php'

    @staticmethod
    def claim(response):
        return response.url.startswith(TopMenu.url)

    @staticmethod
    def parse_page(text):
        soup = bs4.BeautifulSoup(text, 'html.parser')
        moons = soup.find('table', id='themoons')
        for moon in moons.find_all('img'):
            TopMenu.parse_moon(moon)

    @staticmethod
    def parse_moon(moon):
        if 'small' in moon['alt']:
            kolala.moons['small'] = str(moon)
            return
        parts = moon['alt'].split(', ')
        kolala.moons[parts[0]] = parts[1]

    def auto_action(self):
        TopMenu.parse_page(self.response.text)
        return None
