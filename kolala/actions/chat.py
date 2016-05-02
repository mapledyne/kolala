import threading
import time

import kolala
import kolala.framework.Chat as Chat



class ChatThread(threading.Thread):

    def run(self):
        self.stopping = False
        while not kolala.globals.stopping and not self.stopping:
            print("Checking Chat")
            time.sleep(3)
            # call a function


def start_chat():
    kolala.Client.getpage('mchat.php')
    chat_thread.start()

chat_thread = ChatThread()


def main(arg):
    print("." + arg + ".")
    if len(arg) == 0:
        start_chat()
    if arg == "stop":
        print("Stopping chat monitoring...")
        chat_thread.stopping = True
