import kolala


def main(arg):
    print(kolala.banner('Quests'))
    quests = kolala.player.quests
    for quest in quests:
        print(unicode(quests[quest]).encode('utf-8'))
