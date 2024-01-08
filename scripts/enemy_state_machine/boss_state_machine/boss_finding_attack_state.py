from enemy_state_machine.enemy_base_state import EnemyBaseState
from time import time
from player import Player
from math import sqrt


class BossFindingAttackState(EnemyBaseState):
    level = 1

    def enter_state(self):
        ("ENTERED FINDING ATTACK STATE")
        self.change_sub_state(self.enemy.state_factory.chasing(self.enemy))

    def update_state(self):
        pass

    def check_switch_states(self):
        player_distance = sqrt((Player.instance.x_pos - self.enemy.x_pos)**2 + (Player.instance.y_pos - self.enemy.y_pos)**2)

        for attack in self.enemy.ATTACKS:
            if player_distance <= attack.max_distance and player_distance >= attack.min_distance:

                if time() > attack.cooldown + attack.last_shot:

                    self.change_state(attack.attack(
                        self.enemy.state_factory, self.enemy))

                    break

    def exit_state(self):
        pass
