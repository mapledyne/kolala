import requests
import six

from pykol.framework.PageSelector import PageSelector


class Client(object):

    session = requests.Session()

    @staticmethod
    def _dict_to_query_params(d):
        """Return proper query string to add to a url.

        Turns {'count': 5, 'offset': 2} into '?count=5&offset=2'.
        """
        if d is None or len(d) == 0:
            return ''

        param_list = [param + '=' +
                      (str(value).lower()
                       if type(value) == bool else str(value))
                      for param, value in six.iteritems(d)
                      if value is not None]
        return '?' + "&".join(param_list)

    @staticmethod
    def get(url, params=None):
        """Send a  request to the server."""
        if params is None:
            params = {}

        url += Client._dict_to_query_params(params)

        response = Client.session.get(url)

        return response

    @staticmethod
    def post(url, data=None, params=None):
        """Send a  request to the server."""
        if params is None:
            params = {}

        if data is None:
            data = {}

        url += Client._dict_to_query_params(params)

        response = Client.session.post(url, data)

        return response

    @staticmethod
    def getpage(url, params=None):
        response = Client.get(url, params)

        web = PageSelector(response)

        page = web.page()

        req = page.auto_action()
        while req is not None:
            page = PageSelector(req).page()
            req = page.auto_action()

        if type(page).__name__ is 'MainFrame' and url is not page.url:
            return Client.getpage(url, params)
        return page
