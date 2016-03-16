import sys

import pykol.framework as framework

app = framework.KoLCmd()

app.cmdloop()

framework.Client.get('logout.php')
