import pykol


def main(arg):
    print('Campground: {}'.format(pykol.player.home))
    if pykol.player.witchess:
        print('You have a Witchess set.')
