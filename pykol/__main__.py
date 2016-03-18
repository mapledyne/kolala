import sys

import pykol.Config as Config
import pykol.framework as framework
from pykol.framework.Logging import Logging

app = framework.KoLCmd()

app.cmdloop()

framework.Client.get('logout.php')

if Config.save_pages:
    Logging.info('Pages saved under uuid: {}'.format(framework.Client.uuid))
