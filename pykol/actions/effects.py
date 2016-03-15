import pykol


def main(arg):
    print(' Effects '.center(78, '='))
    effects = pykol.player.effects
    for effect in effects:
        print(u'{}'.format(effect))
        if effect.name in pykol.modifiers['Effect']:
            info = pykol.modifiers['Effect'][effect.name]['modifier']
            for i in info:
                print u'\t{}'.format(i)
