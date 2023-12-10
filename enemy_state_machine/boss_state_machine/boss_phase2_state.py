from enemy_state_machine.enemy_base_state import EnemyBaseState
from enemy_state_machine.boss_state_machine.attacks.charge import Charge
from enemy_state_machine.boss_state_machine.attacks.orbs import Orbs
from enemy_state_machine.boss_state_machine.attacks.blast import Blast
from enemy_state_machine.boss_state_machine.attacks.orb_frontal import OrbFrontal
from enemy_state_machine.boss_state_machine.attacks.blast_frontal import BlastFrontal


class BossPhase2State(EnemyBaseState):
    ATTACKS = [Charge(), OrbFrontal(), BlastFrontal()]  # TODO

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
        if self.enemy.health < 200:
            self.change_state(self.enemy.state_factory.phase3(self.enemy))
