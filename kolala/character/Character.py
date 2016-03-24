import kolala.character.Stats as Stats
import kolala.framework.Utils as Utils


class Character(object):

    def __init__(self):
        self.name = ''
        self.char_cls = ''
        self.level = ''
        self.stats = Stats.Stats()
        self.hp = Stats.Stat()
        self.mp = Stats.Stat()
        self.meat = 0
        self.adv = 0
        self.liver = 0
        self.drunk = False
        self.fury = 0
        self.furynote = ''
        self.effects = []
        self.hardcore = False
        self.quests = {}
        self.home = ''

        self.inventory = {}

        self.witchess = False

        self.tattoos = set()

    def owns(self, item):
        if item in self.inventory:
            if self.inventory[item] > 0:
                return True
        return False

    def usable(self):
        usable = []
        for i in list(self.inventory):
            # if this thing is usable ...
            usable.append(i)
        return usable

    def worthless(self):
        worthless_things = ['worthless trinket', 'worthless gewgaw',
                            'worthless knick-knack']
        count = 0
        for w in worthless_things:
            if w in self.inventory:
                count += self.inventory[w]
        return count

    def __str__(self):
        core = ''
        if self.hardcore:
            core = ' [Hardcore]'
        header = Utils.banner(u'{} (Level {} {}){}'.format(self.name,
                              self.level,
                              self.char_cls,
                              core))
        stats = 'Mus: {}, Mox: {}, Mys: {}'.format(self.stats.muscle,
                                                   self.stats.moxie,
                                                   self.stats.mysticality)
        drunk = ''
        if self.drunk:
            drunk = ' (drunk)'
        furynote = self.furynote
        if len(furynote) > 0:
            furynote = ' ({})'.format(furynote)
        fury = ''
        if self.fury > 0:
            fury = 'Fury: {}{}\n'.format(self.fury, furynote)

        msg = (header + '\n' +
               stats + '\n' +
               'HP: {}, MP: {}\n'.format(self.hp, self.mp) +
               'Liver: {}{}\n'.format(self.liver, drunk) +
               'Meat: {:,}\n'.format(self.meat) +
               'Adv: {}\n'.format(self.adv) +
               fury)
        msg += 'Effects: ' + '\n'
        if len(self.effects) == 0:
            msg += '\tNone.\n'
        else:
            for e in self.effects:
                msg += u'\t{}\n'.format(e)
        return msg
