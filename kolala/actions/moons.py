import kolala


def main(arg):
    for moon in kolala.moons:
        print('{}: {}'.format(moon, kolala.moons[moon]))
