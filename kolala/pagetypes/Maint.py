import kolala.Globals
from kolala.pagetypes.KoLPage import KoLPage


class Maint(KoLPage):

    url = kolala.Globals.url + 'maint.php'

    @staticmethod
    def claim(response):
        return response.url.startswith(Maint.url)

    def auto_action(self):
        kolala.Globals.maintenance = True
        print('Kingdom of Loathing is in maintenance mode. Try back later.')
        return None
