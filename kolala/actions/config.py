import kolala


def main(arg):
    print(kolala.banner('Config'))
    for c in kolala.config:
        print('{}: {}'.format(c, kolala.config[c]))
