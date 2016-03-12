class Quest(object):
    def __init__(self, name):
        self.name = name
        self.description = ''
        self.subtasks = []

    def __str__(self):
        ret = u'{}\n{}\n'.format(self.name, self.description)
        for sub in self.subtasks:
            ret += u'\t{}\n'.format(sub)
        return ret
