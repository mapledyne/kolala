from pykol.character.Stats import Stats


class Character(object):

    def __init__(self):
        self.name = ''
        self.char_cls = ''
        self.level = ''
        self.stats = Stats()

    def __str__():
        print('Name: ' + self.name)
        print('Class: ' + self.char_cls)
        print('Level: ' + self.level)
        print('Muscle: ' + self.stats.muscle)
        print('Moxie: ' + self.stats.moxie)
        print('mysticality: ' + self.stats.mysticality)
