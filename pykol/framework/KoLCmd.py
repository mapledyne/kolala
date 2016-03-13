from cmd2 import Cmd
import importlib
import inspect
import pykol.Globals as Globals
from pykol.framework.Client import Client
from pykol.pagetypes.CharPane import CharPane
import pkgutil
import pykol.actions


class KoLCmd(Cmd):
    intro = 'Welcome to pykol. A Kingdom of Loathing python interface.'
    prompt = "> "
    file = None

    def __init__(self):
        package = pykol.actions
        for loader, name, is_pkg in pkgutil.walk_packages(package.__path__):
            module = loader.find_module(name).load_module(name)
            if getattr(module, 'main', None) is not None:
                setattr(self, 'do_' + name, module.main)
        Cmd.__init__(self)
#        Client.getpage(CharPane.url)

    # def do_character(self, arg):
    #     character.do_character(self, arg)
    #
    # def do_meat(self, arg):
    #     meat.do_meat(self, arg)
    #
    # def do_quests(self, arg):
    #     quests.do_quests(self, arg)
    #
    # def do_effects(self, arg):
    #     effects.do_effects(self, arg)
