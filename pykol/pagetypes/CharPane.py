import bs4

from pykol.character.Stat import Stat
import pykol.Config as Config
import pykol.Globals as Globals
from pykol.pagetypes.KoLPage import KoLPage


class CharPane(KoLPage):

    url = Config.url + 'charpane.php'

    @staticmethod
    def claim(response):
        return response.url.startswith(CharPane.url)

    @staticmethod
    def parse_page(text, character):
        soup = bs4.BeautifulSoup(text, 'html.parser')
        tag = soup.find('a', href='charsheet.php')
        tag = tag.find_next('a')
        tag = tag.b
        character.name = tag.text
        tag = tag.next_element
        tag = tag.next_element

        bits = list(tag.stripped_strings)
        character.level = bits[0].split()[1]
        character.char_cls = bits[1]
        tag = tag.table

        tag = tag.find_next('table')
        stats = tag.find_all('tr')
        character.stats.muscle = Stat(stats[0].b.text)
        character.stats.moxie = Stat(stats[1].b.text)
        character.stats.mysticality = Stat(stats[2].b.text)
        if len(stats) > 3:
            character.liver = int(stats[3].b.text)
        character.drunk = 'falling-down drunk' in tag.text

        tag = tag.find_next('img', title='Hit Points')
        character.hp = Stat(tag.text)
        tag = tag.find_next('img')
        character.mp = Stat(tag.text)

        tag = tag.find_next('img', title='Meat')
        character.meat = int(tag.text.replace(',', ''))

        tag = tag.find_next('img', title='Adventures Remaining')
        character.adv = int(tag.text)

    def auto_action(self):
        CharPane.parse_page(self.response.text, Globals.player)
        return None
