import kolala


def main(arg):
    # something like:
    #   http://127.0.0.1:60080/inv_use.php?
    #       pwd=ddc9b3bdfda296d5a713a03e3cd8a405&
    #       which=f-1&
    #       whichitem=23
    targets = kolala.utils.find_from_list(kolala.player.usable(), arg)
    if len(targets) == 0:
        print('No usable item of that name found in your inventory.')
        return
    if len(targets) > 1:
        print('I\'m not sure which item you mean:')
        print('\n'.join(targets))
        return
    url = 'inv_use.php'
    params = {'whichitem': 0}
    print('Cannot use {} until item numbers are supported.'.format(targets[0]))
