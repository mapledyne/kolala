import sys

from kolala.Config import config
from kolala.framework.Client import Client
from kolala.framework.KoLCmd import KoLCmd
from kolala.framework.Logging import Logging


def go():

    app = KoLCmd()

    app.cmdloop()

    Client.get('logout.php')

    if config['save_pages']:
        msg = 'Pages saved under uuid: {}'.format(Client.uuid)
        print(msg)
