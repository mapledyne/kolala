import HTMLParser
import json
import os
import requests

response = requests.get('https://sourceforge.net/p/kolmafia/code/HEAD/tree/src/data/items.txt?format=raw')

parser = HTMLParser.HTMLParser()

text = response.text

lines = text.split('\n')

items = []
for line in lines:
    if len(line) == 0:
        continue
    if line.startswith('#'):
        print('Skipping line: ' + line)
        continue
    item = line.split('\t')
    if len(item) < 7:
        print('Skipping line: ' + line)
        continue
    new_item = {}
    new_item['number'] = int(item[0])
    new_item['name'] = parser.unescape(item[1])
    new_item['descid'] = int(item[2])
    new_item['image'] = item[3]
    new_item['use'] = item[4]
    new_item['access'] = item[5]
    new_item['autosell'] = int(item[6])

    new_item['plural'] = ''
    if len(item) == 8:
        new_item['plural'] = item[7]

    # Not strictly needed,  but nice for clarity
    new_item['quest'] = False
    new_item['gift'] = False
    new_item['tradable'] = False
    new_item['discard'] = False

    for a in new_item['access'].split(','):
        if a == 'q':
            new_item['quest'] = True
        if a == 'g':
            new_item['gift'] = True
        if a == 't':
            new_item['tradable'] = True
        if a == 'd':
            new_item['discard'] = True

    for u in new_item['use'].split(', '):
        if u not in ['none', 'food', 'drink', 'spleen', 'avatar',
                     'usable', 'multiple', 'reusable', 'message', 'grow',
                     'hat', 'weapon', 'sixgun', 'offhand', 'container',
                     'shirt', 'pants', 'accessory', 'familiar',
                     'sticker', 'card', 'folder', 'bootspur', 'bootskin',
                     'food helper', 'drink helper', 'zap',
                     'sphere', 'guardian',
                     'combat', 'combat reusable',
                     'single', 'solo', 'curse', 'bounty', 'candy',
                     'matchable', 'fancy']:
            print('Item with unknown use:')
            print(new_item)
        new_item[u] = True
    items.append(new_item)

    alpha_split = {}
    for i in items:
        first = i['name'][0].lower()
        if first not in alpha_split:
            alpha_split[first] = []
        alpha_split[first].append(i)

if not os.path.exists('_imports/items'):
    os.makedirs('_imports/items')

for a in alpha_split:
    with open('_imports/items/' + a + '.json', 'w+') as outfile:
        json.dump(alpha_split[a], outfile, indent=4)
