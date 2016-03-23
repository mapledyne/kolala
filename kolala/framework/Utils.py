import hashlib

from kolala.Config import config


def banner(msg):
    return(' {} '.format(msg).center(config['screen_width'],
                                     config['banner_char']))


def md5hash(text):
    md5 = hashlib.md5()
    md5.update(text)
    return md5.hexdigest()
