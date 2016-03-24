import bs4

from kolala.game.Items import items
import kolala.Globals
from kolala.pagetypes.KoLPage import KoLPage


class Inventory(KoLPage):

    url = kolala.Globals.url + 'inventory.php'

    @staticmethod
    def claim(response):
        return response.url.startswith(Inventory.url)

    @staticmethod
    def parse_page(text):
        soup = bs4.BeautifulSoup(text, 'html.parser')
        types = ['food', 'booze', 'spleen', 'call', 'hats', 'back',
                 'shirts', 'ranged', 'weapons', 'pants',
                 'offhands', 'accs', 'famequips', 'all', 'potions',
                 'combat', 'quest', 'gifts', 'animalbones', 'cards',
                 'manuelitems']
        for t in types:
            thing = soup.find('table', id=str(t))
            if thing is None:
                continue
            for td in thing.find_all('table'):
                if len(td.span.text) == 0:
                    qty = 1
                else:
                    qty = int(td.span.text.replace('(', '').replace(')', ''))
                items[td.b.text].inventory = qty
                # Usage link:
                # print td.a['href']

    def auto_action(self):
        Inventory.parse_page(self.response.text)
        return None
