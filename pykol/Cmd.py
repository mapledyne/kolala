import sys

import pykol.Config as Config
import pykol.framework as framework
from pykol.framework.Logging import Logging


def go():

    app = framework.KoLCmd()

    app.cmdloop()

    framework.Client.get('logout.php')

    if Config.save_pages:
        msg = 'Pages saved under uuid: {}'.format(framework.Client.uuid)
        print msg
