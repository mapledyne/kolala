import pykol


def main(arg):
    if pykol.globals.clovers == -1:
        pykol.Client.getpage('hermit.php')

    print('There are {} clover(s) remaining at the hermit.'.format(pykol.globals.clovers))
    print('You have {} worthless object(s) to trade.'.format(pykol.player.worthless()))
