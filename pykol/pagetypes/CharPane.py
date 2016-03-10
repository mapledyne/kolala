import bs4

import pykol.Config as Config
from pykol.pagetypes.KoLPage import KoLPage
import pykol.Globals as Globals


class CharPane(KoLPage):

    url = Config.url + 'charpane.php'

    @staticmethod
    def claim(response):
        return response.url.startswith(CharPane.url)

    def auto_action(self):
        soup = bs4.BeautifulSoup(self.response.text, 'html.parser')

        tag = soup.find('a', href='charsheet.php')
        tag = tag.find_next('a')
        tag = tag.b
        Globals.player.name = tag.text
        tag = tag.next_element
        tag = tag.next_element
        bits = list(tag.stripped_strings)
        Globals.player.level = bits[0]
        Globals.player.char_cls = bits[1]
        print str(Globals.player)
        return None
