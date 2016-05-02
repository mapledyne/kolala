import sys

import kolala
from kolala.framework.KoLCmd import KoLCmd


def go():
    app = KoLCmd()
    app.cmdloop()
    kolala.globals.stopping = True
    kolala.Client.get('logout.php')

    if kolala.config['save_pages']:
        msg = 'Pages saved under uuid: {}'.format(kolala.Client.uuid)
        print(msg)
