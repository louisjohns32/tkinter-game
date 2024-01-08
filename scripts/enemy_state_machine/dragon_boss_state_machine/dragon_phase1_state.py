from enemy_state_machine.enemy_base_state import EnemyBaseState
from enemy_state_machine.dragon_boss_state_machine.attacks.fire_breath import FireBreath
from enemy_state_machine.boss_state_machine.attacks.charge import Charge
from enemy_state_machine.dragon_boss_state_machine.attacks.blast import Blast
from time import time


class DragonPhase1State(EnemyBaseState):
    ATTACKS = [FireBreath(), Charge(), Blast()]

    def enter_state(self):
        ("ENTERED PHASE 1 STATE")
        self.enemy.ATTACKS = self.ATTACKS
        self.change_sub_state(
            self.enemy.state_factory.finding_attack(self.enemy))

        # TODO put this into __init__ of attack depending on paramater
        self.ATTACKS[2].last_shot = time()

    def update_state(self):
        pass

    def exit_state(self):
        pass

    def check_switch_states(self):
        # check for phase2 switch
        if self.enemy.health < 300:
           self.change_state(self.enemy.state_factory.phase2(self.enemy))
        pass
