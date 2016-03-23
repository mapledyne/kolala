import os
import requests
import six
import uuid

from kolala.framework.Logging import Logging
from kolala.framework.PageSelector import PageSelector
import kolala.Globals


class Client(object):

    session = requests.Session()
    uuid = uuid.uuid4()
    call_count = 0

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
    def _check_url(url):
        if (url.lower().startswith('http://') or
                url.lower().startswith('https://')):
            return url
        return kolala.Globals.url + url

    @staticmethod
    def get(url, params=None):
        """Send a  request to the server."""
        if params is None:
            params = {}

        url = Client._check_url(url)

        url += Client._dict_to_query_params(params)

        Logging.debug('HTTP Get: ' + url)
        response = Client.session.get(url)
        Client.save_page(url, response.text)

        if 'PHPSESSID' in response.cookies:
            kolala.Globals.PHPSESSID = response.cookies['PHPSESSID']

        return response

    @staticmethod
    def post(url, data=None, params=None):
        """Send a  request to the server."""
        if params is None:
            params = {}

        if data is None:
            data = {}

        url = Client._check_url(url)

        url += Client._dict_to_query_params(params)

        Logging.debug('HTTP Post to: ' + url)
        response = Client.session.post(url, data)
        Client.save_page(url, response.text)
        return response

    @staticmethod
    def save_page(url, page):
        from kolala import config

        if not kolala.config['save_pages']:
            return

        if 'call_counter' not in Client.save_page.__dict__:
            Client.save_page.call_counter = 0
        Client.save_page.call_counter += 1

        page_name = url.replace(kolala.Globals.url, '')
        page_name = page_name.replace('?', '-')

        path = kolala.config['save_pages_path'] + str(Client.uuid) + '/'
        if not os.path.exists(path):
                os.makedirs(path)

        file_name = '{}/[{}] {}'.format(path,
                                        Client.save_page.call_counter,
                                        page_name)

        with open(file_name, 'w+') as file:
            file.write(page.encode('utf-8'))

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
