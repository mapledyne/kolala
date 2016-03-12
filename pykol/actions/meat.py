import pykol.Globals as Globals


def do_meat(self, arg):
    self.stdout.write('You have {:,} meat.\n'.format(Globals.player.meat))
