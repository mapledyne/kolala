import bs4

import kolala.Config as Config
import kolala.Globals
from kolala.pagetypes.KoLPage import KoLPage


class Museum(KoLPage):

    # http://127.0.0.1:60080/museum.php?floor=4&place=royalboards
    url = kolala.Globals.url + 'museum.php'

    @staticmethod
    def claim(response):
        return response.url.startswith(Museum.url)

    @staticmethod
    def parse_page(text):
        soup = bs4.BeautifulSoup(text, 'html.parser')

        table = soup.find('table').find('table').find('table')
        rows = table.find_all('tr')
        name = ''
        museum_list = []
        for r in rows:
            if name == '':
                name = r.find_all('u')[1].text
                continue
            rowid = r.find('a', href=True)['href'].rsplit('=', 1)[1]
            parts = r.find_all('td')
            museum_list.append({'name': parts[0].text, 'id': rowid, 'value': parts[2].text})
        kolala.leaderboards.update(name, museum_list)
        print(museum_list)

    def auto_action(self):
        Museum.parse_page(self.response.text)
        return None
