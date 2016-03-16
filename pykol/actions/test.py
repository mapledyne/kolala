import pykol
import pykol.pagetypes


def main(arg):
    filename = pykol.Config.save_pages_path + 'charpane.php'
    with open(filename, 'r') as file:
        text = file.read()
    top = pykol.pagetypes.CharPane.parse_page(text)
