from cmd2 import Cmd
import importlib
import pykol.Globals as Globals
from pykol.actions import *  # noqa
from pykol.framework.Client import Client
from pykol.pagetypes import CharPane


class KoLCmd(Cmd):
    intro = 'Welcome to pykol. A Kingdom of Loathing python interface.'
    prompt = "> "
    file = None

    def __init__(self):
        super(KoLCmd, self).__init__(self)
        Client.getpage(CharPane.url)

    def do_character(self, arg):
        self.stdout.write(Globals.player)

    def do_meat(self, arg):
        meat.do_meat(self, arg)
