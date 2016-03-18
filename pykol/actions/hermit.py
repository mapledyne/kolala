import pykol


def main(arg):
    if pykol.Globals.clovers is None:
        pykol.Client.getpage('hermit.php')

    print('There are {} clover(s) remaining at the hermit.'.format(pykol.Globals.clovers))
    print('You have {} worthless object(s) to trade.'.format(pykol.player.worthless()))
