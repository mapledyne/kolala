import pykol


def main(arg):
    print(' Quests '.center(78, '='))
    quests = pykol.player.quests
    for quest in quests:
        print(unicode(quests[quest]).encode('utf-8'))
