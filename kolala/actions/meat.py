import kolala


def main(arg):
    print('You have {:,} meat.\n'.format(kolala.player.meat))
    print('Modifiers affecting meat drop:')
    meat_count = 0
    for effect in kolala.player.effects:
        if effect.name in kolala.modifiers['Effect']:
            info = kolala.modifiers['Effect'][effect.name]['modifier']
            for i in info:
                if i.startswith('Meat Drop'):
                    meat_count += 1
                    print('\t{} ({})\n\t\t{}'.format(effect.name, effect.duration, i))
    if meat_count == 0:
        print('\tNone.')
