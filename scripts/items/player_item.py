from PIL import Image, ImageTk


class PlayerItem:

    icon_sprite = "../assets/icons/wand-icon.png" # TODO PLACEHOLDER, CHANGE THIS TO BASIC PLACE HOLDER RATHER THAN WAND
    name = ""
    text = ""

    def __init__(self, player):  # TODO Can you use singletons in python???
        self.level = 1
        self.player = player
       # self.icon_sprite = ImageTk.PhotoImage(Image.open(self.icon_sprite))

    def level_up(self):
        self.level += 1
