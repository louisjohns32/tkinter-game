from items.wand import Wand
from items.pinger import Pinger
from items.shuriken import Shuriken
from PIL import ImageTk


class ItemManager: # stores item id dict, 
    items_id_dict = {
        1:Wand,
        2:Pinger,
        3:Shuriken,
    }
    loaded = False


    def load_item_sprites():
        if not ItemManager.loaded:
            for item in ItemManager.items_id_dict.values():
                print(item.icon_sprite)
                print(item)
                item.icon_sprite = ImageTk.PhotoImage(file=item.icon_sprite)
            ItemManager.loaded = True
    