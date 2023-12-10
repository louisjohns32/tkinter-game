from enemy_state_machine.enemy_attacking_state import EnemyAttackingState
from enemy_state_machine.enemy_dead_state import EnemyDeadState
from enemy_state_machine.dragon_boss_state_machine.dragon_phase1_state import DragonPhase1State
from enemy_state_machine.dragon_boss_state_machine.attacks.fire_breath import FireBreathState
from enemy_state_machine.boss_state_machine.boss_finding_attack_state import BossFindingAttackState
from enemy_state_machine.dragon_boss_state_machine.dragon_chasing_state import DragonChasingState
from enemy_state_machine.boss_state_machine.attacks.charge import BossChargingState
from enemy_state_machine.dragon_boss_state_machine.attacks.blast import BlastState
from enemy_state_machine.enemy_moving_to_state import EnemyMovingToState
from enemy_state_machine.dragon_boss_state_machine.dragon_phase2_state import DragonPhase2State


class DragonStateFactory:
    # LEVEL 1 STATES
    def phase1(self, enemy):
        return DragonPhase1State(enemy)

    def phase2(self, enemy):
        return DragonPhase2State(enemy)

# LEVEL 2 STATES
    def finding_attack(self, enemy):
        return BossFindingAttackState(enemy)

    def fireBreath(self, enemy):  # cleave fire
        return FireBreathState(enemy)

    def charging(self, enemy):  # similar to skeleton charge
        return BossChargingState(enemy)

    def blast(self, enemy):  # breath and leave behind fire on each third of the screen periodically, with the breath first breath expiring before the last
        # Have an enemy which is immune to damage, but can be killed by devestate. Spawn 1 for each phase 1.
        return BlastState(enemy)

    def devestate(self, enemy):
        return ___


# LEVEL 3 STATE

    def chasing(self, enemy):  # Under finding_attack
        return DragonChasingState(enemy)

    def attacking(self, enemy):  # Under finding_attack
        return EnemyAttackingState(enemy)

    def moveTo(self, enemy, pos):
        return EnemyMovingToState(enemy, pos)

    def dead(self, enemy):
        return EnemyDeadState(enemy)
