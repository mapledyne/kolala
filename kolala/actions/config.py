import kolala


def main(arg):
    for c in kolala.config:
        print('{}: {}'.format(c, kolala.config[c]))
