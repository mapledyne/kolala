import kolala.Globals


class KoLPage(object):

    url = kolala.Globals.url

    def __init__(self, response):
        self.response = response

    @staticmethod
    def claim(response):
        raise NotImplementedError("Static function claim() must be implemented.")

    def auto_action(self):
        return None
