import kolala


def main(arg):
    if len(arg) == 0:
        print(('To register a new account with {}, run the command:\n'
               '\tregister <playername> <password>\n'
               'For example:\n'
               '\tregister biggie MyCoolPassword123\n'
               'Type "help register" for more information.'
               '').format(kolala.globals.app_name))
        print('')
        if len(kolala.registrations) == 0:
            print('There are no users currently registered.')
        else:
            print('Currently registered accounts:')
            print(', '.join(kolala.registrations))
        return

    args = arg.split(' ', 1)

    if len(args) < 2:
        print('No password supplied. If you want to log in without '
              'remembering a password,\nuse the "login" command instead.')
        return

    user = args[0]
    password = args[1]
    if user in kolala.registrations:
        print('Updating registration for {}...'.format(user))
    else:
        print('Registering {}...'.format(user))
    kolala.registrations.register(user, password)


def help():
    print('Registration help.')
