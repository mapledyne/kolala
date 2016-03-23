import kolala.Globals
from kolala.pagetypes.KoLPage import KoLPage


class MainFrame(KoLPage):

    url = kolala.Globals.url + 'game.php'

    @staticmethod
    def claim(response):
        return response.url.startswith(MainFrame.url)
