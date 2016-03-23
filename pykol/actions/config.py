import pykol


def main(arg):
    for c in pykol.config:
        print('{}: {}'.format(c, pykol.config[c]))
