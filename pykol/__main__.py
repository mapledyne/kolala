import sys

import pykol.Config as Config
import pykol.framework as framework

app = framework.KoLCmd()

app.cmdloop()

framework.Client.get('logout.php')

if pykol.Config.save_pages:
    framework.Logging.Logging.info('Pages saved under uuid: {}'.format(framework.Client.uuid))
