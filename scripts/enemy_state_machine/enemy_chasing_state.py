from enemy_state_machine.enemy_base_state import EnemyBaseState
from Window import Window

import math


class EnemyChasingState(EnemyBaseState):

    def enter_state(self):
        ("ENTERED CHASING STATE")

    def update_state(self):
        # check for player position
        x = self.enemy.player.x_pos - self.enemy.x_pos
        y = self.enemy.player.y_pos - self.enemy.y_pos
        self.angle = math.atan2(y, x)
        # move towards player
        self.enemy.x_pos += math.cos(self.angle) * self.enemy.speed * \
            Window.delta_time * 50
        self.enemy.y_pos += math.sin(self.angle) * self.enemy.speed * \
            Window.delta_time * 50

        # update facing
        if math.cos(self.angle) > 0:
            self.enemy.facing = "right"
        else:
            self.enemy.facing = "left"

        if self.enemy.facing == "left":  # TODO Checking this in an if statement every tick feels messy
            self.enemy.active_anim = self.enemy.walking_left_anim
        else:
            self.enemy.active_anim = self.enemy.walking_right_anim

    def exit_state(self):
        ("EXITING CHASING STATE")

    def check_switch_states(self):
        # check if close to player and can attack
        x = self.enemy.player.x_pos - self.enemy.x_pos
        y = self.enemy.player.y_pos - self.enemy.y_pos

        if abs(x) < 40 and abs(y) < 80:
            self.change_state(self.enemy.state_factory.attacking(
                self.enemy))  # TODO Super messy, maybe change???
