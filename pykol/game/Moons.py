class Moon(object):
    def __init__(self, text=None):
        if text is None:
            self.text = ''
            return
        if 'small' in text:
            self.text = text
            return
        parts = text.split(', ')
        self.text = parts[1]

    def __str__(self):
        return self.text


class Moons(dict):

    def __init__(self):
        super(Moons, self).__init__(self)
        self['small'] = Moon()
        self['Ronald'] = Moon()
        self['Grimace'] = Moon()
