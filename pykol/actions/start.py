import pykol


def main(arg):
    pykol.Client.getpage('charpane.php')
    print('Visiting the campground...')
    pykol.Client.getpage('campground.php')
    print('Getting inventory...')
    pykol.Client.getpage('inventory.php?which=1')
    pykol.Client.getpage('inventory.php?which=1')
    pykol.Client.getpage('inventory.php?which=2')
    pykol.Client.getpage('inventory.php?which=3')
    print('Visiting the hermit...')
    pykol.Client.getpage('hermit.php')
    print('\tHe has {} clovers.'.format(pykol.globals.clovers))
