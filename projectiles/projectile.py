from game_object import GameObject
import math
from time import time
from Window import Window
# TODO Implement object pooling for projectiles and enemies to optimise memory usage


class Projectile(GameObject):
    type = "Projectile"

    def __init__(self, start_pos, direction, player, sprite, duration=3, speed=1, damage=10, penetrate=0, target="enemy", collision_manager=None, radius=32):
        # initialise projectile with given attributes
        super().__init__(sprite, pos=start_pos, collision_manager=collision_manager)
        self._start_pos, self.direction, self.duration, self.speed = start_pos, direction, duration, speed
        self.start_time = time()
        self.player = player
        self.damage = damage
        self.penetrate = penetrate # dictates how many enemies the projectile penetrates before deleting
        self.target = target # tag to target i.e. collide with and deal damage to
        self.hit_objects = [] # stores all hit objects
        self.radius = radius # collider radius of object

    def update(self):
        self.move()
        self.check_duration()
        

        self.handle_enemy_collisions()
            

    def delete(self):

        self.player.obj_manager.delete_object(self)

    def handle_enemy_collisions(self):
        # check collision
        collisions = self.player.collision_manager.check_collision(
            self.x_pos, self.y_pos, self.radius)
        if type(collisions) != bool: # collision is an object
            for collision in collisions:
                if collision.tag == self.target: # collision is target
                    if collision not in self.hit_objects: # collision not hit before
                        collision.take_damage(self.damage)
                        self.penetrate -= 1
                        self.hit_objects.append(collision)
                        # delete object if not enough penetrates
                        if self.penetrate < 0:
                            self.delete()
        else:
            if collisions:
                self.delete()

        # check collisions with dumb enemies
        collisions = self.player.collision_manager.check_collision_dumb_enemies(self.x_pos, self.y_pos, self.radius)
        # sort collisions in descending order, so popping from list doesnt affect the index of subsequent collisions
        collisions = sorted(collisions, key=lambda x:-x[1])
        
        for i,j in collisions:
            self.player.obj_manager.dumb_enemies[i].deal_damage(j, self.damage)

    def move(self):
        self.set_position(self.x_pos + math.cos(self.direction) * self.speed * Window.delta_time * 100,
                    self.y_pos + math.sin(self.direction) * self.speed * Window.delta_time * 100)
    
    def check_duration(self):
        if time() > self.start_time + self.duration:
            self.delete()