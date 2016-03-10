import bs4
import hashlib

import pykol.Config as Config
from pykol.framework.Client import Client
from pykol.pagetypes.KoLPage import KoLPage


class Login(KoLPage):

    url = Config.url + 'login.php'

    @staticmethod
    def claim(response):
        return response.url.startswith(Login.url)

    @staticmethod
    def digest_password(password, challenge):
        md5 = hashlib.md5()
        md5.update(password)
        hash1 = md5.hexdigest()

        md5 = hashlib.md5()
        md5.update(hash1 + ":" + challenge)
        hash2 = md5.hexdigest()
        return hash2

    def auto_action(self):

        soup = bs4.BeautifulSoup(self.response.text, 'html.parser')

        retry = soup(text=re.compile('try again in'))
        if len(retry) > 0:
            raise framework.KoLError(retry[0])

        form = soup.find('form', attrs={'name': 'Login'})
        params = form.find_all('input')
        param_list = {}
        for p in params:
            try:
                param_list[p.attrs['name']] = p.attrs['value']
            except KeyError:
                param_list[p.attrs['name']] = ''

        response = Login.digest_password(Config.password,
                                         param_list['challenge'])
        param_list['response'] = response
        param_list['secure'] = 1
        param_list['loginname'] = Config.user

        return framework.Client.post(Login.url, param_list)
