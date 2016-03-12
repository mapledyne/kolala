import inspect

import pykol.framework as framework
from pykol.pagetypes import *

app = framework.KolCmd()

app.cmdloop()

web = framework.PageSelector(framework.Client.get('http://www.kingdomofloathing.com'))

page = web.page()

req = page.auto_action()
while req is not None:
    page = framework.PageSelector(req).page()
    req = page.auto_action()

web = framework.PageSelector(framework.Client.get('http://www.kingdomofloathing.com/charpane.php'))

page = web.page()

req = page.auto_action()
while req is not None:
    page = framework.PageSelector(req).page()
    req = page.auto_action()


print('Done.')
