import kolala


def main(arg):
    # something like:
    #   http://127.0.0.1:60080/inv_use.php?
    #       pwd=ddc9b3bdfda296d5a713a03e3cd8a405&
    #       which=f-1&
    #       whichitem=23
    targets = kolala.utils.find_from_list(kolala.player.usable, arg)
    print('Possible targets: {}'.format(len(targets)))
    print('\n'.join(targets))
