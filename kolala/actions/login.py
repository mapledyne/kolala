import kolala


def main(arg):

    if len(arg) == 0:
        if len(kolala.registrations) == 0:
            print('No registered users. Login with a user/pass combo, or '
                  '"register" an account.')
            return
        if len(kolala.registrations) > 1:
            print('More than one user is registered, and I don\'t know which\n'
                  'to choose. Try "register" to see who is registered, or '
                  'specify\nwhich one you want, "login kermit"')
            return
        login(list(kolala.registrations)[0])
        return
    combo = arg.split(' ', 1)
    if len(combo) == 1:
        if combo[0] not in kolala.registrations:
            print('I don\'t recognize that user. Is it spelled right?')
            print('Alternately, you may need to "register" it.')
            return
        login(combo[0])
        return
    login(combo[0], combo[1])
    return


def login(user, password=None):
    if password is not None:
        kolala.Globals.user = user
        kolala.Globals.password = kolala.utils.md5hash(password)
    else:
        if user not in kolala.registrations:
            print('Cannot log in as user "{}" without a password.'.format(user))
            print('Supply a password, or "register" the account.')
            return
        kolala.Globals.user = user
        kolala.Globals.password = kolala.registrations[user]['password']
    kolala.Client.getpage('charpane.php')
    return
