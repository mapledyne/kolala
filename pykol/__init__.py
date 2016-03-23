import pykol.Config
import pykol.framework as framework
import pykol.Globals as globals

from pykol.framework.Client import Client
from pykol.framework.Logging import Logging

from pykol.character.Character import Character
from pykol.game.Modifiers import ModifierList
from pykol.game.Moons import Moons
from pykol.game.Outfits import Outfits
from pykol.game.Stores import Stores

player = pykol.Character()
modifiers = ModifierList()
moons = Moons()
outfits = Outfits()
stores = Stores()

config = pykol.Config.Config()

Logging.log_level(pykol.Config.log_level)
