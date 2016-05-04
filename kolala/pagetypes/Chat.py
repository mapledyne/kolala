import bs4
import json
import urllib

import kolala.Config as Config
import kolala.Globals
from kolala.pagetypes.KoLPage import KoLPage

class Chat(KoLPage):

    url = kolala.Globals.url + 'newchatmessages.php'
    start_url = kolala.Globals.url + 'mchat.php'
    sent_url = kolala.Globals.url + 'submitnewchat.php'

    @staticmethod
    def claim(response):
        return (response.url.startswith(Chat.url) or
                response.url.startswith(Chat.start_url) or
                response.url.startswith(Chat.sent_url))

    @staticmethod
    def parse_page(text):
        Chat.parse_messages(text)

    @staticmethod
    def parse_sent_page(text):
        pass

    @staticmethod
    def parse_start_page(text):
        soup = bs4.BeautifulSoup(text, 'html.parser')

    @staticmethod
    def parse_messages(msgs):
        # {
        #   "msgs": [
        #     {
        #       "type": "private",
        #       "msg": "hello",
        #       "who": {
        #         "name": "DeGrassi",
        #         "id": "1063113"
        #       },
        #       "time": "1462307650"
        #     }
        #   ],
        #   "last": "1422733835",
        #   "delay": 3000
        # }

        # {
        #     'delay': 3000,
        #     'last': '1422735773',
        #     'msgs': [
        #         {
        #             'channelcolor': 'green',
        #             'format': '0',
        #             'who':
        #                 {
        #                     'color': 'black',
        #                     'name': 'Xanatosz',
        #                     'id': '2376328'
        #                 },
        #             'mid': '1422735773',
        #             'time': '1462310159',
        #             'msg': 'Do I still need a bunch of combat items for the tower? -hic-',
        #             'type': 'public',
        #             'channel': 'newbie'
        #         }
        #         ]
        # }

        messages = json.loads(msgs)
        for msg in messages["msgs"]:
            chan = msg["type"]
            if (msg["type"] == 'public'):
                chan = msg["channel"]
            print("({}) {}: {}".format(chan, msg["who"]["name"], msg["msg"]))
            if (msg["type"] == 'private' and not msg["who"]["id"] == kolala.player.id):
                response = kolala.chatbot.respond(msg["msg"])
                print("Response: " + response)
                if (len(response) > 0):
                    graf = "/msg {} {}".format(msg["who"]["id"], response)
                    url = 'submitnewchat.php'
                    params = {'playerid': kolala.player.id, 'pwd': kolala.Globals.pwd, "j": 1, "graf": urllib.quote_plus(graf)}
                    print(graf)
                    kolala.Client.getpage(url, params)

    def auto_action(self):
        if (self.response.url.startswith(Chat.url)):
            Chat.parse_page(self.response.text)
        if (self.response.url.startswith(Chat.start_url)):
            Chat.parse_start_page(self.response.text)
        if (self.response.url.startswith(Chat.sent_url)):
            Chat.parse_sent_page(self.response.text)
        return None
