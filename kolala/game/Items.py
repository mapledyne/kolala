import glob
import json

import kolala
from kolala.Config import config
from kolala.game.Modifiers import modifiers
import kolala.Globals


class Item(dict):
    def __init__(self, data):
        super(Item, self).__init__(self)
        self.inventory = 0
        self.closet = 0
        self.storage = 0

        for d in data:
            self[d] = data[d]

        self.number = self['number']

        self.weapon = False
        if 'weapon' in self:
            self.weapon = self['weapon']
        self.usable = False
        if 'usable' in self:
            self.usable = self['usable']
        self.multiple = False
        if 'multiple' in self:
            self.multiple = self['multiple']

    def use(self, qty=1):
        # something like:
        #   http://127.0.0.1:60080/inv_use.php?
        #       pwd=ddc9b3bdfda296d5a713a03e3cd8a405&
        #       which=f-1&
        #       whichitem=23

        if qty < 0:
            print('That doesn\'t make any sense.')
            return
        url = 'inv_use.php'
        params = {'whichitem': self['number'], 'pwd': kolala.Globals.pwd}
        if not self.multiple and qty > 1:
            print('Cannot multi-use {}. Try using them one at a time.'.format(self))
            return
        if self.multiple and qty > 1:
            url = 'multiuse.php'
            params['action'] = 'useitem'
            params['quantity'] = str(qty)
        print(u'Using {}'.format(self))
        kolala.Client.getpage(url, params)

    def __str__(self):
        return self['name']

    def details(self):
        detail = u'{}\n'.format(self['name'])
        if self['name'] in modifiers['Item']:
            info = modifiers['Item'][self['name']]['modifier']
            for mod in info:
                detail += (u'\t{}\n'.format(mod))
                if mod.startswith('Effect:'):
                    effect_name = mod.split('"')[1]
                    if effect_name in modifiers['Effect']:
                        effect = modifiers['Effect'][effect_name]['modifier']
                        for e in effect:
                            detail += (u'\t\t{}\n'.format(e))
        return detail


class Items(dict):

    def __init__(self):
        super(Items, self).__init__(self)

        for filename in glob.glob(config['data_path'] +
                                  '/items/*.json'):
            with open(filename) as data_file:
                data = json.load(data_file)
                for d in data:
                    item = Item(d)
                    self[item['name']] = item

    def find(self, target):
        found = []
        for item in self:
            target_lower = target.lower()
            test = item.lower()
            if test == target_lower:
                return [self[item]]
            if target_lower in test:
                found.append(self[item])
        return found

    def weapons(self):
        found = []
        for i in keys(self):
            if self[i].weapon:
                found.append(self[i])
        return found

items = Items()
