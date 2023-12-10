from PIL import Image, ImageTk
import time as Time

class Animation:
    def __init__(self, spritesheet_path: str, res: tuple, sprites: int, time=50, scale=1, mirror=False, start=0, end=-1, rotation=0, spin=False):
        # time is in ms
        self.sprites = [] # holds all sprites related to animation
         # load spritesheet
        self.spritesheet = Image.open(spritesheet_path)
        sprites_top = self.spritesheet.width / \
            res[0]  # number of sprites on top row
        if spin:
            # store rotated sprites in sprites
            for i in range(sprites-1): 
                self.sprites.append(self.spritesheet.rotate((i * 360)/sprites))
        else:
            # go through spritesheet, cropping individual sprites and adding them to sprites list
            for i in range(sprites):
                x = (i % sprites_top) * res[0]
                y = (i//sprites_top) * res[1]
                if mirror:
                    self.sprites.append(self.spritesheet.crop((x, y, x+res[0], y+res[1])).resize(
                        (int(res[0]*scale), int(res[1]*scale)), resample=Image.NEAREST).transpose(Image.FLIP_LEFT_RIGHT))

                else:
                    self.sprites.append(self.spritesheet.crop((x, y, x+res[0], y+res[1])).resize(
                        (int(res[0]*scale), int(res[1]*scale)), resample=Image.NEAREST).rotate(rotation, expand=1))
            if end != -1:
                # TODO this could be done better, but i just rushed this solution
                self.sprites = self.sprites[start:end]

        self.time = time/1000  # ms -> s
        self.current_sprite = 0
        self.start_time = Time.time()

    def update(self):
        if Time.time() > self.time + self.start_time:
            # move to next sprite in list
            self.current_sprite += 1
            if self.current_sprite >= len(self.sprites):
                # move back to start of list in circular fashion
                self.current_sprite = 0
            self.start_time = Time.time()

    def get_sprite(self):
        # returns current sprite
        return self.sprites[self.current_sprite]
