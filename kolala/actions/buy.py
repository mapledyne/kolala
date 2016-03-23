import kolala


def main(arg):
    targets = kolala.stores.find(arg)
    if len(targets) == 0:
        print('Could not find that item for sale, sorry.')
        return
    if len(targets) > 1:
        print('Your request could mean multiple things:')
        for t in targets:
            print('\t{}'.format(t))
        return
    offer = targets[0]

    if offer.price > kolala.player.meat:
        print('{} is too expensive. You only have {:,} meat.'.format(offer.name, kolala.player.meat))
        return

    print('Buying {}'.format(offer.name))
    kolala.stores.buy(offer)
