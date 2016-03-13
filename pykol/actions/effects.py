import pykol.Globals as Globals


def main(self, arg):
    self.stdout.write(' Effects '.center(78, '='))
    self.stdout.write('\n')
    effects = Globals.player.effects
    for effect in effects:
        self.stdout.write(unicode(effect))
        self.stdout.write('\n')
