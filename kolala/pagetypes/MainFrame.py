import kolala.Config as Config
from kolala.pagetypes.KoLPage import KoLPage


class MainFrame(KoLPage):

    url = Config.url + 'game.php'

    @staticmethod
    def claim(response):
        return response.url.startswith(MainFrame.url)
