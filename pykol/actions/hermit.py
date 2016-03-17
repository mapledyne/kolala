import pykol


def main(arg):
    if pykol.Globals.clover is None:
        pykol.Client.getpage('hermit.php')

    print('There are {} clovers remaining at ' +
          'the hermit.'.format(pykol.Global.clovers))
    print('You have {} worthless objects to ' +
          'trade.'.format(pykol.player.worthless()))
