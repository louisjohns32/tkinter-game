from projectiles.enemy_orb_projectile import EnemyOrbProjectile


class EnemyBlastProjectile(EnemyOrbProjectile):
    tag = ""
    duration = 5

    def update(self):
        super().update()
        # check collision with enemy orb
        collision = self.player.collision_manager.check_collision_objects(
            self.x_pos, self.y_pos, 32, tag="orb")
        (f"Collison = {collision}")
        if collision != False:
            self.delete()
