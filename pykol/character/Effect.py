class Effect(object):
    def __init__(self, text=''):
        if text == '':
            return
        effect = text.rsplit(' ', 1)
        self.name = effect[0]
        self.duration = int(effect[1].replace('(', '').replace(')', ''))

    def __str__(self):
        return u'{} ({})'.format(self.name, self.duration)
