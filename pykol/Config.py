import os

version = '1.0.0'

log_level = 20

url = 'http://www.kingdomofloathing.com/'

if 'KOL_USER' not in os.environ:
    print('Please set the environment variable \'KOL_USER\' before running.')
    exit(1)
if 'KOL_PASS' not in os.environ:
    print('Please set the environment variable \'KOL_PASS\' before running.')
    exit(1)

user = os.environ['KOL_USER']
password = os.environ['KOL_PASS']

prompt = '\nHP: ${hp} | MP: ${mp} | Meat: ${meat}\n${name}, Level ${level} ${class} > '

data_path = 'pykol/data'

# Variables that are set during runtime:

maintenance = False

# Debug and debug-related variables:
save_pages = True
save_pages_path = '/tmp/pykol/pages/'
