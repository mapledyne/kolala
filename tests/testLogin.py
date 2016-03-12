import bs4
import re
import sys

sys.path.append('..')
import pykol.framework as framework  # noqa


with open('../_pages/login.php', 'r') as file:
    text = file.read()

soup = bs4.BeautifulSoup(text, 'html.parser')
print(text)
retry = soup(text=re.compile('try again in'))
print(retry)
if len(retry) > 0:
    raise framework.KoLError(retry[0])
