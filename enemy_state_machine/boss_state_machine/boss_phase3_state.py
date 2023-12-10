from enemy_state_machine.enemy_base_state import EnemyBaseState
from enemy_state_machine.boss_state_machine.attacks.charge import Charge
from enemy_state_machine.boss_state_machine.attacks.orbs import Orbs
from enemy_state_machine.boss_state_machine.attacks.blast import Blast


class BossPhase3State(EnemyBaseState):
    ATTACKS = [Charge(), Orbs(), Blast()]  # TODO

    def enter_state(self):
        ("ENTERED PHASE 1 STATE")
        self.enemy.ATTACKS = self.ATTACKS
        # Move to center of screen
        self.change_sub_state(
            self.enemy.state_factory.finding_attack(self.enemy))

    def update_state(self):
        pass

    def exit_state(self):
        pass

    def check_switch_states(self):
        # check for phase3 switch
        pass
