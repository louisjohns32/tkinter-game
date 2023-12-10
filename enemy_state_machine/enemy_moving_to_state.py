from enemy_state_machine.enemy_base_state import EnemyBaseState
from math import atan2
import math


class EnemyMovingToState(EnemyBaseState):
    def __init__(self, enemy, pos):
        super().__init__(enemy)
        self.direction = atan2(-self.enemy.y_pos +
                               pos[1], pos[0]-self.enemy.x_pos)
        self.target = pos

    def enter_state(self):
        pass

    def update_state(self):
        self.enemy.x_pos += math.cos(self.direction) * self.enemy.speed * \
            self.enemy.player.state_manager.PLAYING.delta_time * 50
        self.enemy.y_pos += math.sin(self.direction) * self.enemy.speed * \
            self.enemy.player.state_manager.PLAYING.delta_time * 50

    def exit_state(self):
        pass

    def check_switch_states(self):
        # check if moved past target
        if math.sqrt((-self.enemy.y_pos+self._target[1])**2 + (self._target[0]-self.enemy.x_pos)**2) < 5:
            self.change_state(None)
