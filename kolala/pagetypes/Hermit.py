import bs4

import kolala.Config as Config
from kolala.framework.Logging import Logging
import kolala.Globals as Globals
from kolala.pagetypes.KoLPage import KoLPage
import re


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
        try:
            Globals.clovers = int(re.search('\d', str(clover)).group(0))
        except ValueError:
            Logging.error('Something weird happened on the way to the ' +
                          'hermit. Clover count doesn\'t make sense: ' +
                          clover)

    def auto_action(self):
        Hermit.parse_page(self.response.text)
        return None
