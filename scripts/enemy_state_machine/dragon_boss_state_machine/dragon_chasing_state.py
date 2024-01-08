from enemy_state_machine.enemy_chasing_state import EnemyChasingState
from math import radians


class DragonChasingState(EnemyChasingState):
    def update_state(self):
        super().update_state()
        (self.angle)
        if self.angle < 0:
            self.angle += radians(360)
        if self.angle >= radians(45) and self.angle < radians(135):
            self.enemy.active_anim = self.enemy._flying_down
            self.enemy.facing = "down"
        elif self.angle >= radians(135) and self.angle < radians(225):
            self.enemy.active_anim = self.enemy._flying_left
            self.enemy.facing = "left"
        elif self.angle >= radians(225) and self.angle < radians(315):
            self.enemy.active_anim = self.enemy._flying_up
            self.enemy.facing = "up"
        else:
            self.enemy.active_anim = self.enemy._flying_right
            self.enemy.facing = "right"
