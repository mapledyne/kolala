
class Stat(object):

    def __init__(self, val=''):
        self.base = 0
        self.current = 0
        self.separator = ''
        self.parse_stat(val)

    def parse_stat(self, val):
        if len(val) is 0:
            return
        try:
            self.current = int(val)
            self.base = self.current
        except ValueError:
            self.separator = ''
            if '/' in val:
                self.separator = '/'
            both = val.replace('/', '').split()
            self.current = int(both[0])
            self.base = int(both[1].replace(')', '').replace('(', ''))

    def __str__(self):
        if len(self.separator) > 0:
            return '{} {} {}'.format(self.current, self.separator, self.base)
        if self.base == self.current:
            return str(self.base)
        return '{} ({})'.format(self.current, self.base)


class Stats(object):
    def __init__(self):
        self.muscle = Stat()
        self.moxie = Stat()
        self.mysticality = Stat()
