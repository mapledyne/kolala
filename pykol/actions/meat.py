import pykol


def main(arg):
    print('You have {:,} meat.\n'.format(pykol.player.meat))
    print('Modifiers affecting meat drop:')
    meat_count = 0
    for effect in pykol.player.effects:
        if effect.name in pykol.modifiers['Effect']:
            info = pykol.modifiers['Effect'][effect.name]['modifier']
            for i in info:
                if i.startswith('Meat Drop'):
                    meat_count += 1
                    print('\t{} ({})\n\t\t{}'.format(effect.name, effect.duration, i))
    if meat_count == 0:
        print('\tNone.')
