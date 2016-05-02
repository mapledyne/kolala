import bs4
import hashlib
import re

import kolala.framework
import kolala.Globals
from kolala.pagetypes.KoLPage import KoLPage


class Login(KoLPage):

    url = kolala.Globals.url + 'login.php'

    @staticmethod
    def claim(response):
        return response.url.startswith(Login.url)

    @staticmethod
    def digest_password(password, challenge):
        hash2 = kolala.utils.md5hash(kolala.utils.md5hash(password) + ":" + challenge)
        return hash2

    def auto_action(self):
        from kolala.framework.Client import Client

        soup = bs4.BeautifulSoup(self.response.text, 'html.parser')

        retry = soup(text=re.compile('try again in'))
        if len(retry) > 0:
            raise kolala.framework.KoLLoginError(retry[0])

        retry = soup(text=re.compile('Bad password.'))
        if len(retry) > 0:
            raise kolala.framework.KoLLoginError(retry[0])

        form = soup.find('form', attrs={'name': 'Login'})
        params = form.find_all('input')
        param_list = {}
        for p in params:
            try:
                param_list[p.attrs['name']] = p.attrs['value']
            except KeyError:
                param_list[p.attrs['name']] = ''

        response = Login.digest_password(kolala.Globals.password,
                                         param_list['challenge'])
        param_list['password'] = kolala.Globals.password
        param_list['response'] = response
        param_list['secure'] = 1
        param_list['loginname'] = kolala.Globals.user

        print('Logging in as {}...'.format(kolala.Globals.user))

        return Client.post(Login.url, param_list)
