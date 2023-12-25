from enemy_state_machine.boss_state_machine.attacks.boss_base_attack import BossBaseAttack
from time import time
from enemy_state_machine.enemy_base_state import EnemyBaseState
from math import cos, sin, radians
from projectiles.enemy_orb_projectile import EnemyOrbProjectile
from PIL import Image, ImageTk


class Orbs(BossBaseAttack):
    cooldown = 2.5

    def attack(self, state_factory, enemy):
        self.last_shot = time()
        return state_factory.orbing(enemy)


class BossOrbingState(EnemyBaseState):
    sprite = "assets/projectiles/enemyorb-projectile.png"
    charge_time = 0.5
    num_projectiles = 30
    speed = 6
    duration = 5

    def __init__(self, enemy):
        super().__init__(enemy)
        self.sprite = ImageTk.PhotoImage(Image.open(self.sprite))

    def enter_state(self):
        for i in range(self.num_projectiles):
            # TODO get rid of magic numbers
            direction = i*radians(360)/self.num_projectiles
            self.enemy.player.obj_manager.new_object(EnemyOrbProjectile((self.enemy.x_pos + 100 * cos(direction), self.enemy.y_pos + 100 * sin(
                direction)), direction, self.enemy.player, self.sprite, charge_time=self.charge_time, speed=self.speed, duration=self.duration))

        self.start_time = time()

    def update_state(self):
        # move orb projectiles with enemy
        pass

    def check_switch_states(self):
       # once time has passed, exit state
        if time() > self.start_time + self.charge_time + 0.2:

            self.change_state(
                self.enemy.state_factory.finding_attack(self.enemy))

    def exit_state(self):
        # fire projectiles
        pass
