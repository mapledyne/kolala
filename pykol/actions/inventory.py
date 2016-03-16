import pykol


def main(arg):
    print(' Inventory '.center(78, '='))
    for i in pykol.player.inventory:
        name = i
        qty = pykol.player.inventory[i]
        print(u'{} ({})'.format(name, qty))
        if name in pykol.modifiers['Item']:
            info = pykol.modifiers['Item'][name]['modifier']
            for mod in info:
                print(u'\t{}'.format(mod))
                if mod.startswith('Effect:'):
                    effect_name = mod.split('"')[1]
                    if effect_name in pykol.modifiers['Effect']:
                        effect = pykol.modifiers['Effect'][effect_name]['modifier']
                        for e in effect:
                            print(u'\t\t{}'.format(e))
