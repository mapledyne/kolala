import pykol


def main(arg):
    for moon in pykol.moons:
        print('{}: {}'.format(moon, pykol.moons[moon]))
