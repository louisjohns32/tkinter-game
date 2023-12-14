from enemy_state_machine.boss_state_machine.attacks.boss_base_attack import BossBaseAttack
from time import time
from enemy_state_machine.enemy_base_state import EnemyBaseState
from math import atan2, sqrt, radians
from game_object import GameObject
from animation import Animation
from PIL import ImageTk


class FireBreath(BossBaseAttack):
    cooldown = 7

    def attack(self, state_factory, enemy):
        self.last_shot = time()
        return state_factory.fireBreath(enemy)


class FireBreathState(EnemyBaseState):
    duration = 3
    spread = 40  # breath spread in degrees
    max_distance = 400  # breath distance
    damage = 10

    def enter_state(self):
        self.start_time = time()

        (self.enemy.facing)
        if self.enemy.facing == "left":
            pos = (self.enemy.x_pos - 226, self.enemy.y_pos)
            self.direction = radians(180)
        elif self.enemy.facing == "right":
            pos = (self.enemy.x_pos + 226, self.enemy.y_pos)
            self.direction = radians(0)
        elif self.enemy.facing == "up":
            pos = (self.enemy.x_pos, self.enemy.y_pos-160)
            self.direction = radians(90)
        else:
            pos = (self.enemy.x_pos, self.enemy.y_pos+160)
            self.direction = radians(270)

        self.projectile = FireBreathProjectile(
            "", pos=pos, dir=self.enemy.facing)
        self.enemy.player.obj_manager.new_object(self.projectile)

    def update_state(self):
        # TODO maybe move into collision manager?
        player_pos = self.enemy.player.x_pos, self.enemy.player.y_pos
        angle_toplayer = atan2(
            player_pos[1] - self.enemy.y_pos, player_pos[0] - self.enemy.x_pos)
        if abs(self.direction - angle_toplayer) < self.spread/2:
            player_distance = sqrt(
                (player_pos[0] - self.enemy.x_pos)**2 + (player_pos[1] - self.enemy.y_pos)**2)
            if player_distance <= self.max_distance:
                self.enemy.player.take_damage(
                    self.damage * self.enemy.player.state_manager.PLAYING.delta_time)

    def exit_state(self):
        self.enemy.player.obj_manager.delete_object(self.projectile)

    def check_switch_states(self):
        if time() > self.start_time + self.duration:
            # Change to findingattack state
            self.change_state(
                self.enemy.state_factory.finding_attack(self.enemy))


class FireBreathProjectile(GameObject):
    

    def __init__(self, sprite, pos=(0, 0), dir="left"):
        super().__init__(sprite, pos=pos)
        self.animations = {
        "left": Animation("cyberpunk-pack/fire-breath.png", (64, 64), 9, time=16, scale=5, rotation=270),
        "right": Animation("cyberpunk-pack/fire-breath.png", (64, 64), 9, time=16, scale=5, rotation=90),
        "up": Animation("cyberpunk-pack/fire-breath.png", (64, 64), 9, time=16, scale=5, rotation=180),
        "down": Animation("cyberpunk-pack/fire-breath.png", (64, 64), 9, time=16, scale=5)
    }
        self.active_anim = self.animations[dir]


    def update(self):
        self.active_anim.update()
        self.sprite = ImageTk.PhotoImage(self.active_anim.get_sprite())
