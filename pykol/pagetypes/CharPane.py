import bs4

import pykol.Character as Character
import pykol.Config as Config
from pykol.pagetypes.KoLPage import KoLPage


class CharPane(KoLPage):

    url = Config.url + 'charpane.php'

    @staticmethod
    def claim(response):
        return response.url.startswith(CharPane.url)

    def auto_action(self):
        soup = bs4.BeautifulSoup(self.response.text)

        tag = soup.find('a', href='charsheet.php')
        tag = tag.find_next('a')
        tag = tag.b
        Character.name = tag.text
        tag = tag.next_element
        tag = tag.next_element
        bits = list(tag.stripped_strings)
        Character.level = bits[0]
        Character.char_cls = bits[1]
        print Character.name
        print Character.level
        print Character.char_cls
        return None
