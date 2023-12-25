from dumb_objects.dumb_object import DumbObject
from animation import Animation
from player import Player
from Window import Window
from math import atan2, sin, cos
from camera import Camera


class EnemyDumb(DumbObject):
    # overwriteable constant stats
    MAX_HEALTH = 10
    SPEED = 1

    # animations every dumb enemy should have
    move_l_anim_args = []
    move_l_anim_kwargs = {}
    move_r_anim_args = []
    move_r_anim_kwargs = {}

    def __init__(self, *args):
        super().__init__()
        if self.move_l_anim_args:
            self.move_l_anim = Animation(*self.move_l_anim_args,
                                     **self.move_l_anim_kwargs)
            self.move_r_anim = Animation(*self.move_r_anim_args, 
                                     **self.move_r_anim_kwargs)

    def update(self):
        for enemy in self.obj_list:
            position = enemy["position"]
            if abs(position[0] - Player.instance.x_pos) < 60\
            and abs(position[1] - Player.instance.y_pos) < 60:
                Player.instance.take_damage(20*Window.delta_time)
            else:
                direction = atan2((Player.instance.y_pos - position[1]),
                                    (Player.instance.x_pos - position[0]))
                enemy["position"] = (position[0] + cos(direction) * self.SPEED * Window.delta_time * 50
                                     , position[1] + sin(direction)* self.SPEED * Window.delta_time * 50)
                
        self.move_l_anim.update()
        self.move_r_anim.update()
                
    def draw_to_screen(self, canvas):
        for enemy in self.obj_list:
            if Player.instance.collision_manager.check_collision_screen(*enemy["position"])[0]:
                continue
            x = enemy["position"][0]
            y = enemy["position"][1]
            # get position relative to camera
            x = x-Camera.instance.x_pos
            y = y-Camera.instance.y_pos
            # get position on screen
            x += (Window.WIDTH/2) 
            y += (Window.HEIGHT/2)
            if Player.instance.x_pos - enemy["position"][0] < 0:
                canvas.create_image(x,y,image=self.move_l_anim.get_sprite())
            else:
                canvas.create_image(x,y,image=self.move_r_anim.get_sprite())
    def add_object(self, position:tuple):
        self.obj_list.append({"position" : position, "health":self.MAX_HEALTH})

    def deal_damage(self, index, damage):
        self.obj_list[index]["health"] -= damage
        if self.obj_list[index]["health"] <= 0:
            Player.instance.obj_manager.dumb_objects[0].add_object((self.obj_list[index]["position"]))    # TODO URGENT!!!! CHANGE THIS 
            self.obj_list.pop(index)
            



