from enemy_state_machine.boss_state_machine.attacks.boss_base_attack import BossBaseAttack
from enemy_state_machine.enemy_base_state import EnemyBaseState
from projectiles.projectile import Projectile
from time import time
import random as rand
from Window import Window
from animation import Animation
from PIL import ImageTk


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

    def __init__(self, enemy, left, next_state=None):
        super().__init__(enemy)
        self.left = left
        self.next_state = next_state

    def enter_state(self):
        if self.left:
            self.dir = -1
        else:
            self.dir = 1

        self.enemy.player.obj_manager.new_object(DevestateProjectile((self.enemy.x_pos, self.enemy.y_pos),self.enemy))


    def update_state(self):
        self.enemy.x_pos += self.dir * self.enemy.speed * 200 * Window.delta_time

    def exit_state(self):
        pass

    def check_switch_states(self):
        if self.enemy.collision_manager.check_collision_screen(self.enemy.x_pos, self.enemy.y_pos)[0]:
            if self.next_state:
                self.change_state(self.next_state)
            else:
                self.super_state.change_state(self.enemy.state_factory.phase1(self.enemy))


class DevestateProjectile(Projectile):
    time_to_complete = 2
    def __init__(self, pos,enemy):
        # init animation
        self.main_anim = Animation("assets/magma-ground.png",(256,256),1,time=10000)
        self.speed = 0
        self.direction = 0
        self.radius = 64
        self.start_time = time()
        self.x_pos, self.y_pos = pos
        self.enemy = enemy
        print("DEV PROJ")
        pass

    def update(self):
        # check collision
        obj = self.enemy.collision_manager.check_collision_square(self.x_pos,self.y_pos,self.radius, tag="Player")
        if obj:
            obj.take_damage(20)

        self.sprite = ImageTk.PhotoImage(self.main_anim.get_sprite())
        pass

    def draw_to_screen(self, pos, canvas):
        print("RENDER")
        progress = (time()-self.start_time)/self.time_to_complete
        progress *= Window.WIDTH
        tiles_width = progress//(Window.SCALE*256)
        for i in range(int(tiles_width)):
            canvas.create_image(pos[0]+(Window.SCALE*256*i),pos[1],image=self.sprite)
        
    

