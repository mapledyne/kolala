import pykol
import pykol.pagetypes


def main(arg):
    filename = pykol.Config.save_pages_path + 'account_tattoos.php'
    with open(filename, 'r') as file:
        text = file.read()
    top = pykol.pagetypes.Tattoos.parse_page(text)

    for t in pykol.player.tattoos:
        print t
