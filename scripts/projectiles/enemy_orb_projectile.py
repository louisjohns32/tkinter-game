from projectiles.projectile import Projectile
from time import time


class EnemyOrbProjectile(Projectile):
    tag = "orb"

    def __init__(self, start_pos, direction, player, sprite, duration=10, speed=10, damage=10, penetrate=0, radius=15, start_angle=0, charge_time=3):

        super().__init__(start_pos, direction, player, sprite, duration, speed, damage,
                         penetrate, target="player", collision_manager=player.collision_manager)
        self.charge_time = charge_time
        self.start_time = time()

    def update(self):
        # TODO can do this better without the if statements, can use shoot method and call it from boss state
        if time() > self.start_time + self.charge_time:
            super().update()
