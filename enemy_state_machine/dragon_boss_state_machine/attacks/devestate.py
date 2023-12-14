from enemy_state_machine.boss_state_machine.attacks.boss_base_attack import BossBaseAttack
from enemy_state_machine.enemy_base_state import EnemyBaseState
from projectiles.projectile import Projectile
from time import time


class Devestate(BossBaseAttack):
    cooldown = 10

    def attack(self, state_factory, enemy):
        self.last_shot = time()
        return state_factory.devestate(enemy)


class DevestateState(EnemyBaseState):
  #  duration = 3
   # spread = 40 #breath spread in degrees
   # max_distance = 400 #breath distance

    sprite_path = "cyberpunk-pack/devestate.png"

    def enter_state(self):
        pass

    def update_state(self):
        pass

    def exit_state(self):
        pass

    def check_switch_states(self):
        pass


class DevestateProjectile(Projectile):
    def update(self):
        pass

