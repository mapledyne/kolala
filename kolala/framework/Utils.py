from kolala.Config import config


def banner(msg):
    return(' {} '.format(msg).center(config['screen_width'],
                                     config['banner_char']))
