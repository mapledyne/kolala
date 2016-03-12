import bs4

with open('../../_pages/charpane.php', 'r') as file:
    text = file.read()

soup = bs4.BeautifulSoup(text)

tag = soup.find('a', href='charsheet.php')
tag = tag.find_next('a')
tag = tag.b
print 'name: ' + tag.text
tag = tag.next_element
tag = tag.next_element
bits = list(tag.stripped_strings)
level = bits[0]
char_cls = bits[1]
print level
print char_cls
#print 'Extract: ' + str(tag.br.text)
# while tag is not None:
#     print tag
#     tag = tag.next_element
