from items.player_weapon import PlayerWeapon
import math
from projectiles.laser_projectile import LaserProjectile
from time import time
from Window import Window


class Laser(PlayerWeapon):
    icon_sprite = "../assets/icons/wand-icon.png"
    projectile_sprite = "../assets/projectiles/laser.png"

    speed = 5
    penetrate = 5
    cooldown = 10

    name = "Laser"
    level_map = {
        2: {"COOLDOWN" : 9}, 
        3: {"COOLDOWN" : 8}, 
        4: {"COOLDOWN" : 7}, 
        5: {"COOLDOWN" : 6}, 
        6: {"COOLDOWN" : 5}, 
        7: {"COOLDOWN" : 4}, 
        8: {"COOLDOWN" : 4}, 
        9: {"COOLDOWN" : 4}, 
        10: {"COOLDOWN" : 4}, 
                 }

    def shoot_projectile(self, projectiles):
        # get mouse positon
        mouse_x, mouse_y = self.player.input_handler.get_mouse_pos()
        # get direction to mouse pos
        # TODO Get rid of magic numbers
        direction = math.atan2(mouse_y - Window.HEIGHT/2, mouse_x - Window.WIDTH/2)

        self.player.obj_manager.new_object(LaserProjectile(
            (self.player.x_pos, self.player.y_pos), direction, self.player, self.projectile_sprite, 3))
        self.last_shot = time()

