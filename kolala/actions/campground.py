import kolala


def main(arg):
    print(kolala.banner('Campground'))
    print('Campground: {}'.format(kolala.player.home))
    if kolala.player.witchess:
        print('You have a Witchess set.')
