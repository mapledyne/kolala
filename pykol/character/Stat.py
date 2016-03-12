class Stat(object):

    def __init__(self, val=''):
        self.base = 0
        self.current = 0
        self.parse_stat(val)

    def parse_stat(self, val):
        if len(val) is 0:
            return

        try:
            self.current = int(val)
            self.base = self.current
        except ValueError:
            both = val.replace('/', '').split()
            self.current = int(both[0])
            self.base = int(both[1].replace(')', '').replace('(', ''))

    def __str__(self):
        if self.base == self.current:
            return str(self.base)
        return '{} ({})'.format(self.current, self.base)
