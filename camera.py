from time import time
from Window import Window

class Camera:

    def __init__(self):
        self.locked = False
        self.x_pos = 0
        self.y_pos = 0
        self.shaking = False
        self.count = -1
        self.shake_time = 0

    def set_position(self, x, y):
        if not self.locked:
            self.x_pos = x
            self.y_pos = y

    def get_edges(self):
        # returns edges of screen - bottom left coords , top right coords
        return (self.x_pos-Window.WIDTH/2, self.y_pos-Window.HEIGHT/2), (self.x_pos+Window.WIDTH/2, self.y_pos+Window.HEIGHT/2)

    def lock_pos(self, locked):
        # lock position of camera
        self.locked = locked

    def update(self):
        # shake camera if shaking
        if self.shaking: # could be done better in a state, instead of checking shaking every tick
            self.count += 1
            self.x_pos += -10 + (20 * (self.count % 2))
            self.y_pos += -10 + (20 * (self.count % 2))
            if time() > self.shake_time + 2:
                self.shaking = False

    def shake(self):
        self.shaking = True
        self.shake_time = time()
