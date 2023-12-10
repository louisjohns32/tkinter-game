from enemy_state_machine.enemy_base_state import EnemyBaseState
from enemy_state_machine.boss_state_machine.attacks.charge import Charge
from enemy_state_machine.boss_state_machine.attacks.orb_frontal import OrbFrontal


class BossPhase1State(EnemyBaseState):
    ATTACKS = [Charge(), OrbFrontal()]

    def enter_state(self):
        ("ENTERED PHASE 1 STATE")
        self.enemy.ATTACKS = self.ATTACKS
        self.change_sub_state(
            self.enemy.state_factory.finding_attack(self.enemy))

    def update_state(self):
        pass

    def exit_state(self):
        pass

    def check_switch_states(self):
        # check for phase2 switch
        if self.enemy.health < 400:
            self.change_state(self.enemy.state_factory.phase2(self.enemy))
