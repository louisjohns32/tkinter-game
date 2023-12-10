from projectiles.projectile import Projectile
from math import radians, sin, cos, atan2
from time import time
from animation import Animation
from PIL import ImageTk


class ShurikenProjectile(Projectile):
    def __init__(self, start_pos, direction, player, sprite, duration=3, speed=1, damage=10, penetrate=0, radius=15, start_angle=0, target="enemy"):
        super().__init__(start_pos, direction, player, sprite,
                         duration, speed, damage, penetrate, target=target)
        self.animation = Animation("assets/projectiles/shuriken.png",(148,148),16,10,1,spin=True) # TODO i should get rid of the magic string here

    def update(self):
        super().update()
        self.animation.update()
        self.sprite = ImageTk.PhotoImage(self.animation.get_sprite())
        

