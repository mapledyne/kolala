import threading
import time
import urllib

import kolala
import kolala.framework.Chat as Chat


class ChatThread(threading.Thread):

    def run(self):
        self.stopping = False
        while not kolala.globals.stopping and not self.stopping:
            kolala.Client.getpage('newchatmessages.php?j=1')
            time.sleep(3)
            # call a function


def start_chat():
    kolala.Client.getpage('mchat.php')
    chat_thread.start()

chat_thread = ChatThread()


def main(arg):
    if len(arg) == 0:
        start_chat()
        return
    if arg == "stop":
        print("Stopping chat monitoring...")
        chat_thread.stopping = True
        return
#        /submitnewchat.php?playerid='+playerid+'&pwd='+pwdhash+'&graf='+URLEncode(txt)+'&j=1'
    url = 'submitnewchat.php'
    params = {'playerid': kolala.player.id, 'pwd': kolala.Globals.pwd, "j": 1, "graf": urllib.quote_plus(arg)}
    kolala.Client.getpage(url, params)
