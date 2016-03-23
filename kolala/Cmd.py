import sys

import kolala.Config as Config
import kolala.framework as framework
from kolala.framework.Logging import Logging


def go():

    app = framework.KoLCmd()

    app.cmdloop()

    framework.Client.get('logout.php')

    if Config.save_pages:
        msg = 'Pages saved under uuid: {}'.format(framework.Client.uuid)
        print(msg)
