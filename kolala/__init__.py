from kolala.Config import config
import kolala.framework as framework
import kolala.Globals as globals

from kolala.framework.Client import Client
from kolala.framework.Logging import Logging

from kolala.character.Character import Character
from kolala.game.Modifiers import ModifierList
from kolala.game.Moons import Moons
from kolala.game.Outfits import Outfits
from kolala.game.Stores import Stores

player = Character()
modifiers = ModifierList()
moons = Moons()
outfits = Outfits()
stores = Stores()

Logging.log_level(config['log_level'])