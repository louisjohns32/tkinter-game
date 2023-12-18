from projectiles.projectile import Projectile
from math import radians, pi
from animation import Animation
from PIL import ImageTk
from Window import Window



class OrbitorProjectile(Projectile):
    tag = "orb"

    def __init__(self, start_pos, direction, player, sprite, duration=3, speed=1, damage=10, penetrate=0, radius=15, start_angle=0):
        super().__init__(start_pos, direction, player, sprite,
                         duration, speed, damage, penetrate, target="enemy")

        # calculate amount direction should be increased by each update
        circum = pi * radius * 2
        time_to_orbit = circum / self.speed
        self.direction_change = radians(360)/time_to_orbit
        self.direction = start_angle

        self.animation = Animation("assets/projectiles/orbitors-projectile.png",(67,67),7,20,0.75) # TODO i should get rid of the magic string here

    def update(self):
        # update direction
        self.direction += self.direction_change * Window.delta_time * 100
        super().update()
        # move projectile
        self.set_position(
            self.x_pos + self.player.pos_diff[0], self.y_pos + self.player.pos_diff[1])
        # update animation
        self.animation.update()
        self.sprite = ImageTk.PhotoImage(self.animation.get_sprite())
