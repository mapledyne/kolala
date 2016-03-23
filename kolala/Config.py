import json
import os
import kolala.Globals

version = '1.0.0'

log_level = 20

url = 'http://www.kingdomofloathing.com/'

#user = os.environ['KOL_USER']
#password = os.environ['KOL_PASS']

prompt = '\nHP: ${hp} | MP: ${mp} | Meat: ${meat}\n${name}, Level ${level} ${class} > '

data_path = 'kolala/data'


# Debug and debug-related variables:
save_pages = True
save_pages_path = '/tmp/kolala/pages/'

home_path = '/tmp/.{}/'.format(kolala.Globals.app_name)

defaults = {'home_path': '/tmp/.{}/'.format(kolala.Globals.app_name),
            'save_pages': True,
            'save_pages_path': '/tmp/{}/pages/'.format(kolala.Globals.app_name),
            'data_path': '{}/data'.format(kolala.Globals.app_name),
            'prompt': '\nHP: ${hp} | MP: ${mp} | Meat: ${meat}\n${name}, Level ${level} ${class} > ',
            'log_level': 20}


class Config(dict):

    def __init__(self):
        super(Config, self).__init__(self)
        self['config_file'] = home_path + 'config.json'

        for d in defaults:
            self[d] = defaults[d]
        if not os.path.exists(home_path):
            os.makedirs(home_path)
        if not os.path.exists(self['config_file']):
            with open(self['config_file'], 'w+') as openfile:
                openfile.write('')

        with open(self['config_file'], 'r') as configfile:
            text = configfile.read()
        if len(text) == 0:
            return
        try:
            text_json = json.loads(text)
            for j in text_json:
                self[j] = text_json[j]
        except ValueError:
            print('Error parsing the config file located at:')
            print(self['config_file'])
            print('It may not be valid JSON.')
            return

config = Config()
