import pykol
import pykol.pagetypes


def main(arg):
    filename = pykol.Config.save_pages_path + 'inventory.php'
    with open(filename, 'r') as file:
        text = file.read()
    top = pykol.pagetypes.Inventory.parse_page(text)
