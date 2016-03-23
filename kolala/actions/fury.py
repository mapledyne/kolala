import kolala


def main(arg):
    qty = 'gallons'
    if kolala.player.fury == 1:
        qty = 'gallon'
    msg = 'You have {} {} of fury'.format(kolala.player.fury, qty)
    if len(kolala.player.furynote) > 0:
        msg += (', giving you {}'.format(kolala.player.furynote))
    else:
        msg += '.'
    print(msg)
