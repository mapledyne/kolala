import pykol


def main(arg):
    outfits = pykol.outfits
    if arg == 'all':
        for o in outfits:
            print(outfits[o])
        return

    player = pykol.player
    for o in outfits:
        set_list = ''
        owns_part = False
        for p in outfits[o].parts:
            if player.owns(p):
                owns_part = True
                set_list += u'\n\t\u2611 ' + p
            else:
                set_list += u'\n\t\u2610 ' + p
        if owns_part:
            print(u'{}:{}'.format(o, set_list))
            if outfits[o].tattoo not in player.tattoos:
                print(u'\t>> You have not earned a tattoo with this outfit.')
