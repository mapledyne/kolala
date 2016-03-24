import kolala


def main(arg):
    targets = kolala.items.find(arg)
    if len(targets) == 0:
        print('Could not find that item, sorry.')
        return
    if len(targets) > 1:
        print('Your request could mean multiple things:')
        for t in targets:
            print(u'\t{}'.format(t))
        return
    item = targets[0]

    print(item.details())
