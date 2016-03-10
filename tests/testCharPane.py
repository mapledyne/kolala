import bs4
import sys

sys.path.append('..')
import pykol.Character as Character  # noqa


with open('../_pages/charpane.php', 'r') as file:
    text = file.read()

soup = bs4.BeautifulSoup(text)

tag = soup.find('a', href='charsheet.php')
tag = tag.find_next('a')
tag = tag.b
Character.name = tag.text
tag = tag.next_element
tag = tag.next_element
bits = list(tag.stripped_strings)
Character.level = bits[0]
Character.char_cls = bits[1]

tag = tag.table

tag = tag.find_next('table')
stats = tag.find_all('tr')
Character.muscle = stats[0].b.text
Character.moxie = stats[1].b.text
Character.mysticality = stats[2].b.text
Character.str()
