import bs4

import kolala.Config as Config
import kolala.Globals
from kolala.pagetypes.KoLPage import KoLPage


class Chat(KoLPage):

    url = kolala.Globals.url + 'newchatmessages.php'
    start_url = kolala.Globals.url + 'mchat.php'

    @staticmethod
    def claim(response):
        return (response.url.startswith(Chat.url) or response.url.startswith(Chat.start_url))

    @staticmethod
    def parse_page(text):
        soup = bs4.BeautifulSoup(text, 'html.parser')

    @staticmethod
    def parse_start_page(text):
        soup = bs4.BeautifulSoup(text, 'html.parser')

    def auto_action(self):
        if (self.response.url.startswith(Chat.url)):
            Chat.parse_page(self.response.text)
        if (self.response.url.startswith(Chat.start_url)):
            Chat.parse_start_page(self.response.text)
        return None
