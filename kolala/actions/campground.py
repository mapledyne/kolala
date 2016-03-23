import kolala


def main(arg):
    print('Campground: {}'.format(kolala.player.home))
    if kolala.player.witchess:
        print('You have a Witchess set.')
