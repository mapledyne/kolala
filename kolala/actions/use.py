import kolala


def main(arg):
    targets = kolala.utils.find_from_list(kolala.player.usable(), arg)
    if len(targets) == 0:
        print('No usable item of that name found in your inventory.')
        return
    if len(targets) > 1:
        print('I\'m not sure which item you mean:')
        print('\n'.join(targets))
        return
    item = kolala.items[targets[0]]
    item.use()
