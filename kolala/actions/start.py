import kolala


def main(arg):
    kolala.Client.getpage('charpane.php')
    print('Visiting the campground...')
    kolala.Client.getpage('campground.php')
    print('Getting inventory...')
    kolala.Client.getpage('inventory.php?which=1')
    kolala.Client.getpage('inventory.php?which=1')
    kolala.Client.getpage('inventory.php?which=2')
    kolala.Client.getpage('inventory.php?which=3')
    print('Visiting the hermit...')
    kolala.Client.getpage('hermit.php')
    print('\tHe has {} clovers.'.format(kolala.globals.clovers))
