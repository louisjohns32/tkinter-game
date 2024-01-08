from enemy_state_machine.boss_state_machine.attacks.boss_base_attack import BossBaseAttack
from time import time
from enemy_state_machine.enemy_base_state import EnemyBaseState
from math import atan2, sqrt, radians, sin, cos, degrees
from game_object import GameObject
from animation import Animation
from PIL import ImageTk, Image
from projectiles.projectile import Projectile


class Blast(BossBaseAttack):
    cooldown = 10

    def attack(self, state_factory, enemy):
        self.last_shot = time()
        return state_factory.blast(enemy)


# TODO IMPLEMENT min distance, max dinstance FOR ATTACKS TO BE CHECKED IN FINGING ATTACK STATE
class BlastState(EnemyBaseState):
  #  duration = 3
   # spread = 40 #breath spread in degrees
   # max_distance = 400 #breath distance

    sprite_path = "../assets/cyberpunk-pack/devestate.png"

    def enter_state(self):
        direction = atan2(self.enemy.player.y_pos - self.enemy.y_pos,
                          self.enemy.player.x_pos - self.enemy.x_pos)
        print(f"ORIGINAL DIRECITON = {direction}")
        self.projectile_sprite = ImageTk.PhotoImage(
            Image.open(self.sprite_path).rotate(360-degrees(direction)))
        self.projectile = BlastProjectile((self.enemy.x_pos, self.enemy.y_pos), direction, self.enemy.player,
                                          sprite=self.projectile_sprite, penetrate=100, speed=40, radius=128, damage=50)
        self.enemy.player.obj_manager.new_object(self.projectile)

    def update_state(self):
        pass

    def exit_state(self):
        pass

    def check_switch_states(self):
        if self.projectile.awake == False:
            print("PROJETILE IS NOT AWAKE")
            self.change_state(
                self.enemy.state_factory.finding_attack(self.enemy))


class BlastProjectile(Projectile):
    def update(self):
        print(f"DIRECTIOn = {self.direction}")

        self.set_position(self.x_pos + cos(self.direction) * self.speed,
                    self.y_pos + sin(self.direction) * self.speed)
        if time() > self.start_time + self.duration:
            self.delete()  # TODO Use pooling to reuse object instead of deleting. Much better memory optimisation by using pooling

        # check collision
        collision = self.player.collision_manager.check_collision_objects(
            self.x_pos, self.y_pos, 32, tag="player")
        if type(collision) != bool:
            if collision not in self.hit_objects:
                collision.take_damage(self.damage)
                self.penetrate -= 1
                print(f"Penetrate decremented  to {self.penetrate}")
                self.hit_objects.append(collision)
                if self.penetrate < 0:
                    self.delete()
        else:
            if collision:
                self.delete()

        print(f"END OF UPDATE, AWAKE = {self.awake}")
