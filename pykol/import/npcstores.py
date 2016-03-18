import json
import os
import requests

response = requests.get('https://sourceforge.net/p/kolmafia/code/HEAD/tree/src/data/npcstores.txt?format=raw')

text = response.text

lines = text.split('\n')

stores = {}
for line in lines:
    if len(line) == 0:
        continue
    if line.startswith('#'):
        print('Skipping line: ' + line)
        continue
    item = line.split('\t')
    if len(item) < 4:
        print('Skipping line: ' + line)
        continue
    store = item[0]
    url = item[1]
    thing = item[2]
    price = int(item[3])
    row = ''
    if len(item) == 5:
        try:
            row = int(item[4].replace('ROW', ''))
        except ValueError:
            print('No row found for: ' + line)
    if store not in stores:
        stores[store] = {}
    item = {'name': thing, 'url': url, 'price': price, 'row': row}
    stores[store][thing] = item

if not os.path.exists('_imports/npcstores'):
    os.makedirs('_imports/npcstores')

for st in stores:
    with open('_imports/npcstores/' + st + '.json', 'w+') as outfile:
        json.dump({st: stores[st]}, outfile, indent=4)
