import pykol


def main(arg):
    qty = 'gallons'
    if pykol.player.fury == 1:
        qty = 'gallon'
    msg = 'You have {} {} of fury'.format(pykol.player.fury, qty)
    if len(pykol.player.furynote) > 0:
        msg += (', giving you {}'.format(pykol.player.furynote))
    else:
        msg += '.'
    print(msg)
