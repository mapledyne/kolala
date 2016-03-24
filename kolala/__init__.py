from kolala.Config import config
import kolala.framework as framework
import kolala.framework.Utils as utils
import kolala.Globals as globals

from kolala.framework.Client import Client
from kolala.framework.Logging import Logging
import kolala.framework.Registrations as Registrations

from kolala.character.Character import Character
from kolala.game.Items import items
from kolala.game.Modifiers import modifiers
from kolala.game.Moons import Moons
from kolala.game.Outfits import Outfits
from kolala.game.Stores import Stores

player = Character()
moons = Moons()
outfits = Outfits()
stores = Stores()

registrations = framework.Registrations.Registrations()

Logging.log_level(config['log_level'])
