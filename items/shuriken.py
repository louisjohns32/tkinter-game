from items.player_weapon import PlayerWeapon
from PIL import ImageTk, Image
from animation import Animation
from time import time
import math
from projectiles.shuriken_projectile import ShurikenProjectile


class Shuriken(PlayerWeapon):
    icon_sprite = "assets/icons/wand-icon.png"
    projectile_sprite = "assets/projectiles/wand-projectile.png"

    speed = 20
    penetrate = 5

    name = "Shuriken"

    

    level_map = {
        2: {"PROJECTILES" : 2}, 
        3: {"DAMAGE" : 15}, 
        4: {"PROJECTILES" : 3, "SPEED" : 25, "COOLDOWN" : 2}, 
        5: {"PENETRATE" : 10}, 
        6: {"PROJECTILES" : 4}, 
        7: {"DAMAGE" : 20}, 
        8: {"PROJECTILES" : 5}, 
        9: {"COOLDOWN" : 1}, 
        10: {"PROJECTILES" : 7}, 
                 }
    
    def shoot_projectile(self, projectiles):
        # get mouse positon
        mouse_x, mouse_y = self.player.input_handler.get_mouse_pos()
        # get direction to mouse pos
        camera_pos = self.player.state_manager.PLAYING.camera.x_pos, self.player.state_manager.PLAYING.camera.y_pos
        deviance = self.player.x_pos - \
            camera_pos[0], self.player.y_pos - camera_pos[1]
        # TODO Get rid of magic numbers
        direction = math.atan2(
            mouse_y - (deviance[1] + 1080/2), mouse_x - (deviance[0] + 1920/2))
        for i in range(projectiles):
            direction = direction + i*math.radians(360)/projectiles
            self.player.obj_manager.new_object(ShurikenProjectile((self.player.x_pos - i, self.player.y_pos - i), direction, self.player,
                                              sprite=self.projectile_sprite, duration=self.duration, speed=self.speed, penetrate=self.penetrate, damage=self.damage, target="enemy"))
        self.last_shot = time()

    
