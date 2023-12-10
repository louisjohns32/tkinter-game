from enemy_state_machine.boss_state_machine.attacks.boss_base_attack import BossBaseAttack
from time import time
from enemy_state_machine.enemy_base_state import EnemyBaseState
from math import atan2, cos, sin, radians
from projectiles.enemy_orb_projectile import EnemyOrbProjectile
from PIL import Image, ImageTk


class OrbFrontal(BossBaseAttack):
    cooldown = 10

    def attack(self, state_factory, enemy):
        self.last_shot = time()
        return state_factory.orbing_frontal(enemy)


class BossOrbingFrontalState(EnemyBaseState):
    sprite = "assets/projectiles/enemyorb-projectile.png"
    charge_time = 1
    num_projectiles = 10
    speed = 20
    duration = 5

    def __init__(self, enemy):
        super().__init__(enemy)
        self.sprite = ImageTk.PhotoImage(Image.open(self.sprite))

    def enter_state(self):
        player_pos = self.enemy.player.x_pos, self.enemy.player.y_pos
        enemy_pos = self.enemy.x_pos, self.enemy.y_pos
        player_angle = atan2(
            player_pos[1] - enemy_pos[1], player_pos[0] - enemy_pos[0])
        # Create orb projectiles
        for i in range(self.num_projectiles):
            # TODO get rid of magic numbers
            direction = player_angle - \
                radians(30) + i*radians(60)/self.num_projectiles
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
