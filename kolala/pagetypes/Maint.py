import kolala.Config as Config
from kolala.pagetypes.KoLPage import KoLPage


class Maint(KoLPage):

    url = Config.url + 'maint.php'

    @staticmethod
    def claim(response):
        return response.url.startswith(Maint.url)

    def auto_action(self):
        Config.maintenance = True
        return None
