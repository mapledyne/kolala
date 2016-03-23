import pykol


def main(arg):
    pykol.Client.getpage(pykol.globals.url + arg)
