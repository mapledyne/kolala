import kolala


def main(arg):
    player = kolala.player
    outfits = kolala.outfits

    outfit_tattoos = []
    non_tattoos = []
    unearned = []

    print('Earned Tattoos:')
    for t in kolala.player.tattoos:
        outfit = ''
        for o in outfits:
            if t == outfits[o].tattoo:
                outfit = outfits[o].name
        if outfit == '':
            non_tattoos.append(t)
        else:
            outfit_tattoos.append(outfit)

    for o in outfits:
        if o not in outfit_tattoos:
            unearned.append(o)

    print('Non-outfit tattoos:')
    if len(non_tattoos) == 0:
        print('\tNone.')
    else:
        print('\t' + '\t\n'.join(non_tattoos))
    print('Outfit tattoos:')
    if len(outfit_tattoos) == 0:
        print('\tNone.')
    else:
        print('\t' + '\n\t'.join(outfit_tattoos))
    print('Unearned outfit tattoos:')
    if len(outfit_tattoos) == 0:
        print('\tNone.')
    else:
        print('\t' + '\t\n'.join(unearned))
