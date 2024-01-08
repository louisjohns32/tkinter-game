from enemy_state_machine.boss_state_machine.attacks.boss_base_attack import BossBaseAttack
from time import time
from enemy_state_machine.enemy_base_state import EnemyBaseState
from math import atan2, cos, sin
from Window import Window

class Charge(BossBaseAttack):
    cooldown = 10

    def attack(self, state_factory, enemy):
        self.last_shot = time()
        return state_factory.charging(enemy)


class BossChargingState(EnemyBaseState):
    def enter_state(self):
        player_pos = self.enemy.player.x_pos, self.enemy.player.y_pos
        enemy_pos = self.enemy.x_pos, self.enemy.y_pos
        self.direction = atan2(
            player_pos[1] - enemy_pos[1], player_pos[0] - enemy_pos[0])
        ("CHARGING")
        self.edges = self.enemy.player.state_manager.PLAYING.camera.get_edges()

    def update_state(self):
        self.enemy.set_position(self.enemy.x_pos + cos(self.direction) * self.enemy.speed * self.enemy.speed
                          * Window.delta_time * 200, self.enemy.y_pos +
                          sin(self.direction) * self.enemy.speed * Window.delta_time * 200)

    def check_switch_states(self):
        # check collision with screen edge #TODO MOVE INTO CHECK COLLISION
        if self.enemy.player.collision_manager.check_collision_screen(self.enemy.x_pos, self.enemy.y_pos)[0]:
            self.change_state(
                self.enemy.state_factory.finding_attack(self.enemy))

    def exit_state(self):
        return super().exit_state()
