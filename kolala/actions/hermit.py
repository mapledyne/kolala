import kolala


def main(arg):
    if kolala.globals.clovers == -1:
        kolala.Client.getpage('hermit.php')

    print('There are {} clover(s) remaining at the hermit.'.format(kolala.globals.clovers))
    print('You have {} worthless object(s) to trade.'.format(kolala.player.worthless()))
