import kolala


def main(arg):
    print(kolala.utils.banner('Inventory'))
    for i in kolala.player.inventory():
        if len(arg) > 0 and arg.lower() not in i.lower():
            continue
        qty = kolala.items[i].inventory
        print(u'{} ({})'.format(i, qty))
        if i in kolala.modifiers['Item']:
            info = kolala.modifiers['Item'][i]['modifier']
            for mod in info:
                print(u'\t{}'.format(mod))
                if mod.startswith('Effect:'):
                    effect_name = mod.split('"')[1]
                    if effect_name in kolala.modifiers['Effect']:
                        effect = kolala.modifiers['Effect'][effect_name]['modifier']
                        for e in effect:
                            print(u'\t\t{}'.format(e))
