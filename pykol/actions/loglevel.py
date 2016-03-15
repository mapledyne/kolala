import pykol


def main(arg):
    if len(arg) == 0:
        print('Log levels can be set from 0-50, corresponding to:')
        print('10: DEBUG')
        print('20: INFO')
        print('30: WARNING')
        print('40: ERROR')
        print('50: CRITICAL')
        print('Current log level is: {}'.format(Logging.log_level()))
    try:
        new = int(arg)
    except ValueError:
        print('Cannot change level to \'{}\''.format(new))
        return
    print('Changing logging level to {}.'.format(new))
    pykol.Logging.log_level(new)
