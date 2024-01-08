from enemy_state_machine.enemy_chasing_state import EnemyChasingState
from enemy_state_machine.enemy_attacking_state import EnemyAttackingState
from enemy_state_machine.enemy_dead_state import EnemyDeadState


class EnemyStateFactory:
    def chasing(self, enemy):
        return EnemyChasingState(enemy)

    def attacking(self, enemy):
        return EnemyAttackingState(enemy)

    def dead(self, enemy):
        return EnemyDeadState(enemy)
