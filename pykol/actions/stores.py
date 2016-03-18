import pykol


def main(arg):
    for s in pykol.stores:
        print(pykol.stores[s].display())
