import glob
import json

from kolala.Config import config


class Modifier(dict):
    def __init__(self, mod):
        super(Modifier, self).__init__(self)
        for m in mod:
            self[m] = mod[m]


class ModifierList(dict):

    def __init__(self):
        super(ModifierList, self).__init__(self)

        for filename in glob.glob(config['data_path'] + '/modifiers/*.json'):
            with open(filename) as data_file:
                data = json.load(data_file)
                for d in data:
                    if data[d]['category'] not in self:
                        self[data[d]['category']] = {}
                    self[data[d]['category']][data[d]['name']] = Modifier(data[d])

modifiers = ModifierList()
