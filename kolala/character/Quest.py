import textwrap


class Quest(object):
    def __init__(self, name):
        self.name = name
        self.description = ''
        self.subtasks = []

    def __str__(self):
        ret = textwrap.fill(u'{}'.format(self.description), 78) + '\n'
        for sub in self.subtasks:
            ret += textwrap.fill(u'\t{}'.format(sub)) + '\n'
        return ret
