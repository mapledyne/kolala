import glob
import json

import kolala


class Offer(object):
    def __init__(self, data):
        self.name = data['name']
        self.price = data['price']
        self.row = data['row']
        self.url = data['url']

    def __str__(self):
        return self.name

    def display(self):
        return '{}: {} meat'.format(self.name, self.price)

    def buy(self, qty=1):
        Stores.buy(self, qty)


class Store(dict):

    def __init__(self, name):
        super(Store, self).__init__(self)
        self.name = name

    def __str__(self):
        return self.name

    def display(self):
        dis = self.name + '\n'
        for i in self:
            dis += '\t{}\n'.format(self[i].display())
        return dis


class Stores(dict):

    def __init__(self):
        super(Stores, self).__init__(self)

        for filename in glob.glob(kolala.config['data_path'] +
                                  '/npcstores/*.json'):
            with open(filename) as data_file:
                data = json.load(data_file)
                for d in data:
                    if d not in self:
                        self[d] = Store(d)
                    for o in data[d]:
                        self[d][o] = Offer(data[d][o])

    def find(self, target):
        found = []
        for store in self:
            for item in self[store]:
                if item == target.lower():
                    return [self[store][item]]
                t_case = target.lower()
                if t_case in item.lower():
                    found.append(self[store][item])
        return found

    def buy(self, offer, qty=1):
        # something like:
        # shop.php?whichshop=generalstore
        #   &action=buyitem&quantity=1
        #   &whichrow=630
        #   &pwd=0c08a016ea730f6457979c89ff9d0d62
        url = ("shop.php?whichshop={}"
               "&action=buyitem&quantity={}"
               "&whichrow={}"
               "&pwd={}").format(offer.url,
                                 str(qty),
                                 str(offer.row),
                                 kolala.globals.pwd)
        kolala.Client.getpage(url)
