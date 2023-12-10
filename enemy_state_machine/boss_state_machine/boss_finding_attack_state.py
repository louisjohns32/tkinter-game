from enemy_state_machine.enemy_base_state import EnemyBaseState
from time import time


class BossFindingAttackState(EnemyBaseState):
    level = 1

    def enter_state(self):
        ("ENTERED FINDING ATTACK STATE")
        self.change_sub_state(self.enemy.state_factory.chasing(self.enemy))

    def update_state(self):
        pass

    def check_switch_states(self):

        for attack in self.enemy.ATTACKS:

            if time() > attack.cooldown + attack.last_shot:

                self.change_state(attack.attack(
                    self.enemy.state_factory, self.enemy))

                break

    def exit_state(self):
        pass
