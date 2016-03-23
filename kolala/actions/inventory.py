import kolala


def main(arg):
    print(kolala.banner('Inventory'))
    for i in kolala.player.inventory:
        name = i
        qty = kolala.player.inventory[i]
        print(u'{} ({})'.format(name, qty))
        if name in kolala.modifiers['Item']:
            info = kolala.modifiers['Item'][name]['modifier']
            for mod in info:
                print(u'\t{}'.format(mod))
                if mod.startswith('Effect:'):
                    effect_name = mod.split('"')[1]
                    if effect_name in kolala.modifiers['Effect']:
                        effect = kolala.modifiers['Effect'][effect_name]['modifier']
                        for e in effect:
                            print(u'\t\t{}'.format(e))
