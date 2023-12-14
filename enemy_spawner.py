from enemies.slime import Slime
from PIL import ImageTk
import random as rand
from math import sin, cos, radians
from enemies.skeleton import Skeleton
from enemies.rat import Rat
from enemies.boss import Boss
from enemies.dragon_boss import DragonBoss
from enemies.flower import Flower
import time


class enemy_spawner:
    # TODO Take hash table from file
    wave_1_map = {0: {Slime: 3},
                  1: {Slime: 5},  # time/5 -> {enemy->rate}
                  2: {Slime: 7},
                  3: {Slime: 7},
                  4: {Slime: 7},
                  5: {Slime: 10},
                  6: {Skeleton: 5, Slime: 10},
                  7: {Skeleton: 5, Slime: 10},
                  8: {Skeleton: 5, Slime: 10},
                  9: {},
                  10: {Skeleton: 10, Slime: 10},
                  11: {Skeleton: 10, Slime: 10},
                  12: {},
                  13: {},
                  14: {Rat: 5},
                  15: {Rat: 20},
                  16: {Slime: 10, Skeleton: 10},  # fix this code
                  17: {Rat: 5, Skeleton: 5},
                  18: {Slime: 10, Skeleton: 10},
                  19: {Rat: 20, Skeleton: 10},
                  20: {},
                  21: {},
                  22: [],
                  23: {},
                  "boss": {Boss: 1}
                  }
    wave_1_map = {"boss" : {DragonBoss : 1}}

    wave_2_map = {
        0: {},
        1: {Flower: 5},
        2: {},
        3: {Flower: 10},
        "boss": {DragonBoss: 1}}

    def __init__(self, start_time: int, obj_manager, player):
        self.spawn_map = [self.wave_1_map.copy(), self.wave_2_map.copy()] # list of waves 

        self.wave = 0
        self.start_time = start_time
        self.obj_manager = obj_manager
        self.player = player
        self.count = 0
        self.enemy_multiplier = 1

    def update(self):
        try:
            for enemy in self.spawn_map[self.wave][(time.time()-self.start_time)//5]:
                # loop for how many enemies need to be spawned
                for _ in range(int(self.spawn_map[self.wave][(time.time()-self.start_time)//5][enemy] * self.enemy_multiplier)):
                    # pick random angle to spawn at
                    angle = rand.randint(0, 360)
                    # set spawn pos based off angle
                    x = self.player.x_pos + cos(radians(angle)) * 1000
                    y = self.player.y_pos + sin(radians(angle)) * 1000
                    # create enemy object
                    self.obj_manager.new_object(enemy(ImageTk.PhotoImage(file="testObj.png"), self.player, pos=(
                        x, y), collision_manager=self.obj_manager.collision_manager))
            
            self.spawn_map[self.wave][(time.time()-self.start_time)//5] = {}
        except Exception as e:
            # Spawn boss
            for enemy in self.spawn_map[self.wave]["boss"]:
                for _ in range(self.spawn_map[self.wave]["boss"][enemy]):
                    # choose random angle to spawn at
                    angle = rand.randint(0, 360)
                    # set pos based off angle
                    x = self.player.x_pos + cos(radians(angle)) * 1000
                    y = self.player.y_pos + sin(radians(angle)) * 1000
                    # create boss object
                    boss = enemy(ImageTk.PhotoImage(file="testObj.png"), self.player, pos=(
                        x, y), collision_manager=self.obj_manager.collision_manager)
                    self.obj_manager.new_object(boss)
                    self.spawn_map[self.wave]["boss"] = {}
                    # set boss state reference to boss object
                    self.player.state_manager.PLAYING.change_sub_state(
                        self.player.state_manager.BOSS)
                    self.player.state_manager.BOSS.set_boss_ref(boss)

    def nextWave(self):
        self.wave += 1
        self.start_time = time.time()
        # CHECK IF END OF WAVES,
        if self.wave >= len(self.spawn_map):
            # CHANGE TO NEGATIVETRAITSTATE TO PICK NEGATIVE TRAIT
            self.enemy_multiplier += 2
            self.spawn_map = [self.wave_1_map.copy(), self.wave_2_map.copy()]
            self.wave = 0

    def save(self):
        save_dict = {}
        save_dict["start_time"] = self.start_time
        save_dict["wave"] = self.wave
        save_dict["multiplier"] = self.enemy_multiplier
        return save_dict

    def load(self, info, save_time):
        # set start_time 
        self.start_time = time.time() - (save_time - info["start_time"])
        self.wave = info["wave"]
        self.enemy_multiplier = info["multiplier"]
