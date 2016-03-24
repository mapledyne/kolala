import hashlib

from kolala.Config import config
import kolala.Globals


def banner(msg):
    return(' {} '.format(msg).center(config['screen_width'],
                                     config['banner_char']))


def md5hash(text):
    md5 = hashlib.md5()
    md5.update(text)
    return md5.hexdigest()


def find_from_list(haystack, needle):
    found = []
    for h in haystack:
        if needle in h:
            found.append(h)
    return found
