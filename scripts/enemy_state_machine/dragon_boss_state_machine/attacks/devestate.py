from enemy_state_machine.boss_state_machine.attacks.boss_base_attack import BossBaseAttack
from enemy_state_machine.enemy_base_state import EnemyBaseState
from projectiles.projectile import Projectile
from time import time
import random as rand
from Window import Window
from animation import Animation
from PIL import ImageTk
from camera import Camera


class Devestate(BossBaseAttack):
    cooldown = 10

    def attack(self, state_factory, enemy):
        self.last_shot = time()
        return state_factory.devestate(enemy)


class DevestateState(EnemyBaseState):
  #  duration = 3
   # spread = 40 #breath spread in degrees
   # max_distance = 400 #breath distance

    sprite_path = "../assets/cyberpunk-pack/devestate.png"

    def __init__(self, enemy, left, next_state=None):
        super().__init__(enemy)
        self.left = left
        self.next_state = next_state

    def enter_state(self):
        if self.left:
            self.dir = -1
        else:
            self.dir = 1

        self.enemy.player.obj_manager.new_object(DevestateProjectile((self.enemy.x_pos, self.enemy.y_pos),self.enemy,self.left),front=True)


    def update_state(self):
        self.enemy.x_pos += self.dir * self.enemy.speed * 200 * Window.delta_time

    def exit_state(self):
        pass

    def check_switch_states(self):
        if self.enemy.collision_manager.check_collision_screen(self.enemy.x_pos, self.enemy.y_pos)[0]:
            if self.next_state:
                self.change_state(self.next_state)
            else:
                self.change_state(self.enemy.state_factory.moveTo(
                    self.enemy,(Camera.instance.get_edges()[int(not self.left)][0] +50 -100 * int(not self.left), self.enemy.player.y_pos),next_state=
                    self.enemy.state_factory.devestate(self.enemy,not self.left),speed_multiplier=2))


class DevestateProjectile(Projectile):
    time_to_complete = 1.5
    time_to_expire = 9
    def __init__(self, pos,enemy,left):
        # init animation
        self.main_anim = Animation("../assets/magma-ground.png",(256,256),1,time=10000)
        self.speed = 0
        self.direction = 0
        self.height = 256
        self.start_time = time()
        self.x_pos, self.y_pos = pos
        self.enemy = enemy
        self.player = enemy.player
        self.sprite = self.main_anim.get_sprite()
        self.left = left
        self.progress = 0

    def update(self):
        self.progress = (time()-self.start_time)/self.time_to_complete

        position = (self.x_pos+((Window.WIDTH/2)*self.progress)/2 - int(self.left)*((Window.WIDTH/2)*self.progress),self.y_pos)
        # check collision - super messy, TODO cleanup
        obj = self.enemy.collision_manager.check_collision_rect(position[0],position[1],
                                                                ((Window.WIDTH/2)*self.progress, self.height/2), tag="player")
        if obj:
            obj.take_damage(100 * Window.delta_time) 

        

        

        if time() > self.start_time + self.time_to_expire:
            self.delete()
        pass

    def draw_to_screen(self, pos, canvas):
        
        width = self.progress * Window.WIDTH
        tiles_width = width//(Window.SCALE*256)
        for i in range(int(tiles_width)):
            canvas.create_image(pos[0]+(Window.SCALE*256*i) - 2* (Window.SCALE*256*i) *(int(self.left)),pos[1],image=self.sprite)
        
    

