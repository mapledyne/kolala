import kolala.Config as Config

class KoLPage(object):

    url = Config.url

    def __init__(self, response):
        self.response = response

    @staticmethod
    def claim(response):
        raise NotImplementedError("Static function claim() must be implemented.")

    def auto_action(self):
        return None
