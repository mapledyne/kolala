import pykol


def main(arg):
    pykol.Client.getpage(pykol.Config.url + arg)
