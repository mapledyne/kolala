import bs4
import sys

sys.path.append('..')
from pykol.character import Character  # noqa
from pykol.pagetypes.CharPane import CharPane  # noqa

with open('../_pages/charpane.php', 'r') as file:
    text = file.read()

char = Character()

CharPane.parse_page(text, char)

print str(char)
exit(0)
