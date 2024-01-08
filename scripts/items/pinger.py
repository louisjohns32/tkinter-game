from items.player_weapon import PlayerWeapon
from PIL import ImageTk, Image
from projectiles.pinger_projectile import PingerProjectile
import math
from time import time
from Window import Window


class Pinger(PlayerWeapon):
    icon_sprite = "../assets/icons/wand-icon.png"
    projectile_sprite = "../assets/projectiles/pinger-projectile.png"

    speed = 30
    penetrate = 5

    name = "Pinger"

    level_map = {2: {"COOLDOWN": 4, "DAMAGE": 10, "PROJECTILES": 2}, 3: {"PROJECTILES": 3, "DAMAGE": 12, "PENETRATE": 10}, 4: {"SPEED": 50, "DAMAGE": 15}, 5: {
        "COOLDOWN": 3, "DAMAGE": 20}, 6: {"PROJECTILES": 4}, 7: {"DAMAGE": 25}, 8: {"COOLDOWN": 2}, 9: {"COOLDOWN": 1}, 10: {"DAMAGE": 30, "PROJECTILES": 5}}

    # TODO CREATE PROJECTILE TYPE ATTRIBUTE, SO shoot_projectile DOESNT HAVE TO BE OVERRIDED AS OFTEN

    def shoot_projectile(self, projectiles):
        # get mouse positon
        mouse_x, mouse_y = self.player.input_handler.get_mouse_pos()
        # get direction to mouse pos
        camera_pos = self.player.state_manager.PLAYING.camera.x_pos, self.player.state_manager.PLAYING.camera.y_pos
        deviance = self.player.x_pos - \
            camera_pos[0], self.player.y_pos - camera_pos[1]
        # TODO Get rid of magic numbers
        direction = math.atan2(
            mouse_y - (deviance[1] + Window.HEIGHT/2), mouse_x - (deviance[0] + Window.WIDTH/2))
        for i in range(projectiles):
            direction = direction + i*math.radians(360)/projectiles
            self.player.obj_manager.new_object(PingerProjectile((self.player.x_pos - i, self.player.y_pos - i), direction, self.player,
                                              sprite=self.projectile_sprite, duration=self.duration, speed=self.speed, penetrate=self.penetrate, damage=self.damage, target="enemy"))
        self.last_shot = time()
