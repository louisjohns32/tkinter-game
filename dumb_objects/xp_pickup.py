from dumb_objects.dumb_object import DumbObject
from animation import Animation
from camera import Camera
from Window import Window
from PIL import ImageTk
from player import Player


class XpPickup(DumbObject):
    def __init__(self):
        super().__init__()
        self.obj_list = []

        self.xp_amnt = 1
        self.animation = Animation("cyberpunk-pack/xp-pickup.png", (64, 64), 1, scale=0.5)
    
    def update(self):
        
        self.sprite = self.animation.get_sprite()

        # check collision with player - TODO this should be optimised
        for i,obj in enumerate(self.obj_list):
            if abs(Player.instance.x_pos -obj[0]) < 120 and abs(Player.instance.y_pos - obj[1]) < 120:
                Player.instance.increaseXP(self.xp_amnt)
                self.obj_list.pop(i)
    
    def draw_to_screen(self, canvas):
        for obj in self.obj_list:
            # get position in world
            x = obj[0]
            y = obj[1]
            # get position relative to camera
            x = x-Camera.instance.x_pos
            y = y-Camera.instance.y_pos
            # get position on screen
            x += (Window.WIDTH/2) 
            y += (Window.HEIGHT/2)

            canvas.create_image(x,y,image=self.sprite)

