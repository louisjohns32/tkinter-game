from enemy_state_machine.enemy_chasing_state import EnemyChasingState
from enemy_state_machine.enemy_attacking_state import EnemyAttackingState
from enemy_state_machine.enemy_dead_state import EnemyDeadState
from enemy_state_machine.boss_state_machine.boss_phase1_state import BossPhase1State
from enemy_state_machine.boss_state_machine.boss_phase2_state import BossPhase2State
from enemy_state_machine.boss_state_machine.boss_finding_attack_state import BossFindingAttackState
from enemy_state_machine.boss_state_machine.attacks.charge import BossChargingState
from enemy_state_machine.boss_state_machine.attacks.orb_frontal import BossOrbingFrontalState
from enemy_state_machine.boss_state_machine.attacks.blast_frontal import BossBlastingFrontalState
from enemy_state_machine.boss_state_machine.attacks.blast import BossBlastingState
from enemy_state_machine.boss_state_machine.attacks.orbs import BossOrbingState
from enemy_state_machine.boss_state_machine.boss_phase3_state import BossPhase3State


class BossStateFactory:
    # LEVEL 1 STATES
    def phase1(self, enemy):
        return BossPhase1State(enemy)

    def phase2(self, enemy):
        return BossPhase2State(enemy)

    def phase3(self, enemy):
        return BossPhase3State(enemy)

    def dead(self, enemy):
        return EnemyDeadState(enemy)

# LEVEL 2 STATES
    def finding_attack(self, enemy):
        return BossFindingAttackState(enemy)

    def charging(self, enemy):
        return BossChargingState(enemy)

    def blasting(self, enemy):
        return BossBlastingState(enemy)

    def orbing(self, enemy):
        return BossOrbingState(enemy)

    def orbing_frontal(self, enemy):
        return BossOrbingFrontalState(enemy)

    def blasting_frontal(self, enemy):
        return BossBlastingFrontalState(enemy)


# LEVEL 3 STATE

    def chasing(self, enemy):  # Under finding_attack
        return EnemyChasingState(enemy)

    def attacking(self, enemy):  # Under finding_attack
        return EnemyAttackingState(enemy)
