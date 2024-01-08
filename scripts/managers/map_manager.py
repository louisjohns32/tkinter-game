from PIL import ImageTk, Image
from Window import Window


class MapManager:
    TILE_SIZE = 128
    MAP_ARRAY = []

    def __init__(self):
        self.TILE_SIZE = self.TILE_SIZE * Window.SCALE
        img = Image.open("../assets/stone-wall.png").resize((128,
                                                          128), resample=Image.NEAREST)
        self.TEXTURE_MAP = {255: ImageTk.PhotoImage(
            file="../assets/grass.png"), 0: ImageTk.PhotoImage(img)}
        # load map image
        self.map_img = Image.open("../assets/map.png")
        # create map array based off image
        self.MAP_ARRAY = [
            [[] for j in range(self.map_img.width)] for i in range(self.map_img.height)]
        print(self.MAP_ARRAY)
        for x in range(self.map_img.width):
            for y in range(self.map_img.height):
                self.MAP_ARRAY[x][y] = self.map_img.getpixel((x, y))[0]
