from time import time
from PIL import Image, ImageTk
from projectiles.projectile import Projectile
import math


class LaserProjectile(Projectile):
    def __init__(self, start_pos, direction, player, sprite, cooldown, duration=3, speed=1, damage=10, penetrate=0, width=16):
        super().__init__(start_pos, direction, player,
                         sprite, duration, speed, damage, penetrate)

        self.x_pos, self.y_pos = start_pos
        self.start_time = time()
        self.charge_time = 1 # TODO pass in as item attribute
        self.width = width
        self.spritePIL = Image.open(
            "assets/projectiles/laser.png").resize((1920, width), resample=Image.NEAREST)
        self.sprite = ImageTk.PhotoImage(self.spritePIL)

    def update(self):
        # get mouse positon
        mouse_x, mouse_y = self.player.input_handler.get_mouse_pos()
        # get direction to mouse pos
        # TODO Get rid of magic numbers
        direction = math.atan2(mouse_y - 1080/2, mouse_x - 1920/2)

       # set sprite alpha

        if time() > self.start_time + self.charge_time:
            self.shoot()
        self.spritePIL.putalpha(
            int((((time()-self.start_time)/self.charge_time)*255)))
        self.sprite = ImageTk.PhotoImage(
            self.spritePIL.rotate(360-math.degrees(direction), expand=1))
        self.x_pos = self.player.x_pos + math.cos(direction)
        self.y_pos = self.player.y_pos + math.sin(direction)

    def shoot(self):
        # get mouse positon
        mouse_x, mouse_y = self.player.input_handler.get_mouse_pos()
        # get direction to mouse pos
        # TODO Get rid of magic numbers
        direction = math.atan2(mouse_y - 1080/2, mouse_x - 1920/2)

        for obj in self.player.collision_manager.check_collision_line(self.x_pos, self.y_pos, width=self.width, angle=direction):
            try:
                if obj != self.player:
                    obj.take_damage(100)
            except Exception as e:
                (e)

        self.delete()

    def get_sprite(self):
        return self.sprite, "player"
