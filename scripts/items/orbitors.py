from items.player_weapon import PlayerWeapon
from projectiles.orbitor_projectile import OrbitorProjectile
from time import time
import math


class Orbitors(PlayerWeapon):
    icon_sprite = "../assets/icons/wand-icon.png"
    projectile_sprite = "../assets/projectiles/orbitors-projectile.png"

    name = "Orbitors"

    cooldown = 6
    radius = 128
    speed = 5
    penetrate = 10
    duration = 3

    level_map = {2: {"COOLDOWN": 4, "DAMAGE": 6, "PROJECTILES": 2}, 3: {"PROJECTILES": 3, "DAMAGE": 7}, 4: {"SPEED": 10, "DAMAGE": 10}, 5: {
        "COOLDOWN": 3, "DAMAGE": 15}, 6: {"PROJECTILES": 4}, 7: {"DAMAGE": 20}, 8: {"COOLDOWN": 2}, 9: {"DAMAGE": 25}, 10: {"PROJECTILES": 5}}

    def shoot_projectile(self, projectiles):
        direction = 0

        angle_per_proj = math.radians(360)/projectiles
        for i in range(projectiles):
            angle = i * angle_per_proj
            pos = (self.player.x_pos + math.cos(angle) * self.radius,
                   self.player.y_pos + math.sin(angle) * self.radius)

            self.player.obj_manager.new_object(OrbitorProjectile(pos,
                                                                direction, self.player, sprite=self.projectile_sprite, duration=self.duration,
                                                                speed=self.speed, penetrate=self.penetrate, radius=self.radius, start_angle=angle + math.radians(90)))
        self.last_shot = time()

        # TESTING PURPOSES
