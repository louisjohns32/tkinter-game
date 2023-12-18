from enemy_state_machine.enemy_base_state import EnemyBaseState
from math import atan2
import math
from Window import Window
from camera import Camera


class EnemyMovingToState(EnemyBaseState):
    def __init__(self, enemy, pos, next_state = None):
        super().__init__(enemy)
        
        self.target = pos
        self.next_state = next_state

    def enter_state(self):
        self.direction = atan2(-self.enemy.y_pos +
                               self.target[1], self.target[0]-self.enemy.x_pos)
        print(f"Entering move to, moving to {self.target}")
        print(f"Cam edges: {Camera.instance.get_edges()}")
        pass

    def update_state(self):
        self.enemy.x_pos += math.cos(self.direction) * self.enemy.speed * \
            Window.delta_time * 50
        self.enemy.y_pos += math.sin(self.direction) * self.enemy.speed * \
            Window.delta_time * 50

    def exit_state(self):
        pass

    def check_switch_states(self):
        # check if moved past target
        deviance = atan2(-self.enemy.y_pos +
                               self.target[1], self.target[0]-self.enemy.x_pos) - self.direction
        if abs(deviance) > 0.5:
            self.change_state(self.next_state)
