from cmd2 import Cmd
import importlib
import inspect
import pkgutil

import pykol
import pykol.actions
from pykol.framework.Client import Client
import pykol.Globals as Globals
from pykol.pagetypes.CharPane import CharPane


class Prompt(object):
    def __str__(self):
        if pykol.player.name == '':
            return ('Not logged in. Try \'login\', or \'register\' to '
                    'add a player to the system.\n> ')
        replacements = {'name': pykol.player.name,
                        'class': pykol.player.char_cls,
                        'level': pykol.player.level,
                        'hp': '{}/{}'.format(pykol.player.hp.current,
                                             pykol.player.hp.base),
                        'mp': '{}/{}'.format(pykol.player.mp.current,
                                             pykol.player.mp.base),
                        'meat': '{:,}'.format(pykol.player.meat)}

        prompt = pyckol.config.prompt
        for r in replacements:
            needle = '${' + r + '}'
            prompt = prompt.replace(needle, replacements[r])
        return prompt


class KoLCmd(Cmd):
    intro = 'Welcome to pykol. A Kingdom of Loathing python interface.'
    prompt = Prompt()
    file = None

    def __init__(self):
        package = pykol.actions
        for loader, name, is_pkg in pkgutil.walk_packages(package.__path__):
            module = loader.find_module(name).load_module(name)
            if getattr(module, 'main', None) is not None:
                setattr(self, 'do_' + name, module.main)
        Cmd.__init__(self)
