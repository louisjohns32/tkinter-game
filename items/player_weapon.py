from items.player_item import PlayerItem
from time import time
from projectiles.projectile import Projectile
import math
from PIL import Image, ImageTk


class PlayerWeapon(PlayerItem):
    level_map = {}  # TODO Store this in JSON file

    damage = 10
    projectile_sprite = None
    cooldown = 3
    penetrate = 0  # Penetrates n enemies
    duration = 3
    speed = 1
    projectiles = 1  # number of projectiles

    last_shot = 0

    def __init__(self, player):
        super().__init__(player)
        self.projectile_sprite = ImageTk.PhotoImage(
            Image.open(self.projectile_sprite))
        self.damage = self.damage
        self.cooldown = self.cooldown
        self.penetrate = self.penetrate  # Penetrates n enemies
        self.duration = self.duration
        self.speed = self.speed
        self.projectiles = self.projectiles  # number of projectile

    def update(self):
        if time() > self.last_shot + self.cooldown:
            self.shoot_projectile(self.projectiles + self.player.projectiles)

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
            self.player.obj_manager.new_object(Projectile((self.player.x_pos - i, self.player.y_pos - i), direction, self.player,
                                              sprite=self.projectile_sprite, duration=self.duration, speed=self.speed, penetrate=self.penetrate, damage=self.damage, target="enemy"))
        self.last_shot = time()

    def level_up(self):
        try:
            super().level_up()
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
        except:
            pass
