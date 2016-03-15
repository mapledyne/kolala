import pykol


def main(arg):
    print(' Inventory '.center(78, '='))
    for i in pykol.player.inventory:
        name = i
        qty = pykol.player.inventory[i]
        print('{} ({})'.format(name, qty))
        if name in pykol.modifiers['Item']:
            info = pykol.modifiers['Item'][name]['modifier']
            for mod in info:
                print(u'\t{}'.format(mod))
