import bs4
import sys

sys.path.append('..')
sys.path.append('.')

from pykol.character import Character  # noqa
import pykol.framework as framework  # noqa
from pykol.pagetypes.CharPane import CharPane  # noqa
import pykol

with open('_pages/charpane.php', 'r') as file:
    text = file.read()

CharPane.parse_page(text, pykol.player)

app = framework.KoLCmd()

app.cmdloop()
