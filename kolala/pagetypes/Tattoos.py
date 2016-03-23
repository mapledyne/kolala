import bs4

import kolala.Config as Config
import kolala.Globals as Globals
from kolala.pagetypes.KoLPage import KoLPage


class Tattoos(KoLPage):

    url = Config.url + 'account_tattoos.php'

    @staticmethod
    def claim(response):
        return response.url.startswith(Tattoos.url)

    @staticmethod
    def parse_page(text):
        soup = bs4.BeautifulSoup(text, 'html.parser')
        form = soup.find('form', action='account_tattoos.php')
        tattoos = form.find_all('img')
        tat_list = set()
        for tat in tattoos:
            tat_list.add(tat['alt'].replace('Tattoo: ', ''))
        Globals.player.tattoos = tat_list

    def auto_action(self):
        Tattoos.parse_page(self.response.text)
        return None
