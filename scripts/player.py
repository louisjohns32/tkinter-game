from game_object import GameObject
from items.shotgun import Shotgun
from items.wand import Wand  # TODO Shouldnt need when fully implemented
from animation import Animation
from PIL import ImageTk
from items.orbitors import Orbitors
from items.laser import Laser
from items.pinger import Pinger
from items.shuriken import Shuriken
from Window import Window
import numpy as np
from items.item_manager import ItemManager


class Player(GameObject):

    instance = None

    max_health = 200
    collidable = True
    radius = 32

    tag = "player" # tag used for collision
    type = "Player" # type used for loading saves

    projectiles = 0  # number of extra projectiles
    speed = 1  # speed multiplier
    duration = 1  # duration multiplier

   

    # TODO i could store this in a json? or come up with better way of loading items without the need for this
    items_mape = {"Pinger": Pinger, "Wand": Wand,
                 "Shotgun": Shotgun, "Orbitors": Orbitors, "Laser": Laser, "Shuriken" : Shuriken}
    
    items_map = {Pinger : None, Wand:None, Shotgun:None, Orbitors:None, Laser:None, Shuriken:None}

    def __init__(self, input_handler, sprite, collision_manager, obj_manager, state_manager):
        Player.instance = self

        super().__init__(sprite, collision_manager=collision_manager)
        self.input_handler = input_handler
        self.obj_manager = obj_manager
        self.leveled = False
        self.state_manager = state_manager
        self.x_pos = 18000
        self.y_pos = 18000

        # STATS
        self.health = self.max_health
        self.level = 0
        self. xp = 0
        self.max_xp = int(5 + self.level * 1.5)

        ItemManager.load_item_sprites()
        self.items = []
        self.items.append(Wand(self))
        self.items_map[Wand] = self.items[0]

         # ANIMATIONS
        self.facing = "r"  # r for right, l for left
        self.idle_l_anim = Animation("../assets/cyberpunk-pack/1 Biker/Biker_idle.png",
                            (20, 34), 4, scale=3, time=120, mirror=True)
        self.idle_r_anim = Animation(
            "../assets/cyberpunk-pack/1 Biker/Biker_idle.png", (20, 34), 4, scale=3,  time=120)

        self.walking_right_anim = Animation(
            "../assets/cyberpunk-pack/1 Biker/Biker_run.png", (34, 32), 6, scale=3, time=80)
        self.walking_left_anim = Animation(
            "../assets/cyberpunk-pack/1 Biker/Biker_run.png", (34, 32), 6, scale=3, time=80, mirror=True)
        
        self.active_anim = self.idle_r_anim


    def update(self):
        idle = True
        pos_before = (self.x_pos, self.y_pos)
        x_movement, y_movement = 0,0
        #check input
        if self.input_handler.get_input_action("up"):
            y_movement-=1
            idle = False
            if self.facing == "l":
                self.active_anim = self.walking_left_anim
            else:
                self.active_anim = self.walking_right_anim

        if self.input_handler.get_input_action("down"):
            if self.facing == "l":
                self.active_anim = self.walking_left_anim
            else:
                self.active_anim = self.walking_right_anim
            y_movement+=1
            idle = False

        if self.input_handler.get_input_action("left"):
            x_movement-=1
            self.active_anim = self.walking_left_anim
            self.facing = "l"
            idle = False

        if self.input_handler.get_input_action("right"):
            x_movement +=1
            self.active_anim = self.walking_right_anim
            idle = False
            self.facing = "r"

        if abs(x_movement) == abs(y_movement) == 1:
            self.set_position(self.x_pos+(self.speed *
                        Window.delta_time * 500 * x_movement)/1.414, self.y_pos + (self.speed *
                        Window.delta_time * 500 * y_movement)/1.414,)
        else:
            self.set_position(self.x_pos+(self.speed *
                        Window.delta_time * 500 )*x_movement, self.y_pos + (self.speed *
                        Window.delta_time * 500)*y_movement,)

        if idle:
            if self.facing == "l":
                self.active_anim = self.idle_l_anim
            else:
                self.active_anim = self.idle_r_anim
        # For projectiles to keep track
        self.pos_diff = (
            self.x_pos - pos_before[0], self.y_pos - pos_before[1])

        # update objects
        for obj in self.items:
            obj.update()

        # update animation
        self.active_anim.update()
        self.sprite = self.active_anim.get_sprite()

    def take_damage(self, dmg):
        self.health = max(0, self.health-dmg)
        if self.health == 0: # if dead
            self.state_manager.PLAYING.change_state(self.state_manager.GAMEOVER)
    def increase_health(self,amnt):
        self.health = min(self.max_health, self.health + amnt)

    def increaseXP(self, amount):
        self.xp += amount

        if self.xp >= self.max_xp:  # if player level up
            self.level_up()

    def addItem(self, itemType):
        # Check if player already has item, if so increase level
        for item in self.items:
            if type(item) == itemType:
                item.level_up()
                return item

        else:  # Else, add item to items
            self.items.append(itemType(self))
            self.items_map[itemType] = self.items[-1]
            return self.items[-1]

    def level_up(self):
        pass
        #self.level += 1
        ## carry over additional xp
        #self.xp = self.xp % int(self.max_xp)
        ## update max_xp
        #self.max_xp = 5 + self.level * 1.5
        #self.leveled = True

    def save(self):
        save_dict = super().save()

        # health, level, xp
        save_dict["health"] = self.health
        save_dict["level"] = self.level
        save_dict["xp"] = self.xp
        # items
        items = {}
        for item in self.items:
            items[item.name] = item.level
        save_dict["items"] = items

        return save_dict

    def load(self, save_dict):
        # load pos
        self.x_pos, self.y_pos = save_dict["position"]
        # load stats
        self.health = save_dict["health"]
        self.level = save_dict["level"]
        self.xp = save_dict["xp"]
        # load player items
        items = []
        for item in save_dict["items"]:
            items.append(self.items_map[item](self))
            for _ in range(save_dict["items"][item]-1):
                items[-1].level_up()

        self.items = items

    def set_position(self, x, y):
        if self.collision_manager.check_collision_wall(x, y, self.radius) and not self.collision_manager.check_collision_screen(x, y)[0]:
            self.x_pos, self.y_pos = x, y
