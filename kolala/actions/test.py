import kolala
import kolala.pagetypes


def main(arg):
    print(kolala.banner('Tattoos'))
    filename = kolala.config['save_pages_path'] + 'account_tattoos.php'
    with open(filename, 'r') as file:
        text = file.read()
    top = kolala.pagetypes.Tattoos.parse_page(text)

    for t in kolala.player.tattoos:
        print(t)
