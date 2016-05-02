import kolala


def main(arg):
    if len(arg) == 0:
        print('Log levels can be set from 0-50, corresponding to:')
        print('10: DEBUG')
        print('20: INFO')
        print('30: WARNING')
        print('40: ERROR')
        print('50: CRITICAL')
        print('Current log level is: {}'.format(kolala.Logging.log_level()))
        return
    try:
        new = int(arg)
    except ValueError:
        print('Cannot change level to \'{}\''.format(new))
        return
    print('Changing logging level to {}.'.format(new))
    kolala.config['log_level'] = new
    kolala.Logging.log_level(new)
