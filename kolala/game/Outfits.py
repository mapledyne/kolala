import glob
import json

from kolala.Config import config


class Outfit(object):
    def __init__(self, data):
        self.name = data['name']
        self.image = data['img']
        self.tattoo = self.image.replace('.gif', '')
        self.parts = data['parts']

    def __str__(self):
        parts_list = ''
        for p in self.parts:
            parts_list += '\n\t{}'.format(p)
        return ('{}:{}'.format(self.name, parts_list))


class Outfits(dict):

    def __init__(self):
        super(Outfits, self).__init__(self)

        for filename in glob.glob(config['data_path'] +
                                  '/outfits/outfits.json'):
            with open(filename) as data_file:
                data = json.load(data_file)
                for d in data:
                    self[d] = Outfit(data[d])
