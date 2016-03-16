import sys

import pykol.Config as Config
import pykol.framework as framework

app = framework.KoLCmd()

app.cmdloop()

# framework.Client.get(Config.url + 'logout.php')
