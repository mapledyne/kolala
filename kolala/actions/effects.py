import kolala


def main(arg):
    print(' Effects '.center(78, '='))
    effects = kolala.player.effects
    for effect in effects:
        print(u'{}'.format(effect))
        if effect.name in kolala.modifiers['Effect']:
            info = kolala.modifiers['Effect'][effect.name]['modifier']
            for i in info:
                print u'\t{}'.format(i)
