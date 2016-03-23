import kolala


def main(arg):
    for s in kolala.stores:
        print(kolala.stores[s].display())
