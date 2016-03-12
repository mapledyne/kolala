from pykol.character.Stat import Stat
from pykol.character.Stats import Stats


class Character(object):

    def __init__(self):
        self.name = ''
        self.char_cls = ''
        self.level = ''
        self.stats = Stats()
        self.hp = Stat()
        self.mp = Stat()
        self.meat = 0
        self.adv = 0
        self.liver = 0
        self.drunk = False
        self.fury = 0

    def __str__(self):
        msg = ('Name: ' + self.name + '\n' +
               'Class: ' + self.char_cls + '\n' +
               'Level: ' + self.level + '\n' +
               'Muscle: ' + str(self.stats.muscle) + '\n'
               'Moxie: ' + str(self.stats.moxie) + '\n'
               'Mysticality: ' + str(self.stats.mysticality) + '\n' +
               'Liver: ' + str(self.liver) + '\n' +
               'Drunk: ' + str(self.drunk) + '\n' +
               'HP: ' + str(self.hp) + '\n' +
               'MP: ' + str(self.mp) + '\n' +
               'Meat: ' + str(self.meat) + '\n' +
               'Adv: ' + str(self.adv) + '\n' +
               'Fury: ' + str(self.fury) + '\n')
        return msg
