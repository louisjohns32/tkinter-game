from items.player_weapon import PlayerWeapon
from PIL import ImageTk, Image
from time import time
import math
from projectiles.projectile import Projectile
from Window import Window


class Shotgun(PlayerWeapon):
    icon_sprite = "assets/icons/wand-icon.png"
    projectile_sprite = "assets/projectiles/shotgun-projectile.png"

    name = "Shotgun"
    text = "BAM"

    speed = 50
    damage = 15  # CHANGE BACK TO 5
    projectiles = 5
    cooldown = 5
    penetrate = 1
    duration = 1

    spread = 10

    level_map = {2: {"COOLDOWN": 4, "DAMAGE": 6}, 3: {"PROJECTILES": 8, "DAMAGE": 7}, 4: {"SPREAD": 20, "DAMAGE": 8, "PROJECTILES": 16}, 5: {
        "COOLDOWN": 3, "DAMAGE": 10}, 6: {"PROJECTILES": 20}, 7: {"DAMAGE": 15}, 8: {"COOLDOWN": 1.5}, 9: {"SPREAD": 30, "PROJECTILE": 30}, 10: {"DAMAGE": 20}}

    def __init__(self, player):
        super().__init__(player)
        self.spread = self.spread

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

            self.player.obj_manager.new_object(Projectile((self.player.x_pos, self.player.y_pos), (direction-math.radians(self.spread/2)) + i*math.radians(
                self.spread)/self.projectiles, self.player, sprite=self.projectile_sprite, duration=self.duration, speed=self.speed, target="enemy"))
        self.last_shot = time()

    def level_up(self):
        self.level += 1
        (self.level_map[self.level])
        for attribute in self.level_map[self.level]:
            if attribute == "DAMAGE":  # Cant use match else as its not running on 3.10 or later
                self.damage = self.level_map[self.level][attribute]
            elif attribute == "PROJECTILES":
                self.projectiles = self.level_map[self.level][attribute]
            elif attribute == "COOLDOWN":
                self.cooldown = self.level_map[self.level][attribute]
            elif attribute == "PENETRATE":
                self.penetrate = self.level_map[self.level][attribute]
            elif attribute == "SPEED":
                self.speed = self.level_map[self.level][attribute]
            elif attribute == "DURATION":
                self.duration = self.level_map[self.level][attribute]
            elif attribute == "SPREAD":
                self.spread = self.level_map[self.level][attribute]
