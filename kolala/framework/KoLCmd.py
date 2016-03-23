from cmd2 import Cmd
import importlib
import inspect
import pkgutil

import kolala
import kolala.actions
from kolala.framework.Client import Client
import kolala.Globals as Globals
from kolala.pagetypes.CharPane import CharPane


class Prompt(object):
    def __str__(self):
        if kolala.player.name == '':
            return ('Not logged in. Try \'login\', or \'register\' to '
                    'add a player to the system.\n> ')
        replacements = {'name': kolala.player.name,
                        'class': kolala.player.char_cls,
                        'level': kolala.player.level,
                        'hp': '{}/{}'.format(kolala.player.hp.current,
                                             kolala.player.hp.base),
                        'mp': '{}/{}'.format(kolala.player.mp.current,
                                             kolala.player.mp.base),
                        'meat': '{:,}'.format(kolala.player.meat)}

        prompt = pyckol.config.prompt
        for r in replacements:
            needle = '${' + r + '}'
            prompt = prompt.replace(needle, replacements[r])
        return prompt


class KoLCmd(Cmd):
    intro = 'Welcome to kolala. A Kingdom of Loathing python interface.'
    prompt = Prompt()
    file = None

    def __init__(self):
        package = kolala.actions
        for loader, name, is_pkg in pkgutil.walk_packages(package.__path__):
            module = loader.find_module(name).load_module(name)
            if getattr(module, 'main', None) is not None:
                setattr(self, 'do_' + name, module.main)
        Cmd.__init__(self)
