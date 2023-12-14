from projectiles.projectile import Projectile
from math import radians, sin, cos, atan2
from time import time
from Window import Window


class PingerProjectile(Projectile):
    def __init__(self, start_pos, direction, player, sprite, duration=3, speed=1, damage=10, penetrate=0, radius=15, start_angle=0, target="enemy"):
        super().__init__(start_pos, direction, player, sprite,
                         duration, speed, damage, penetrate, target=target)

    def update(self):
        #update projectile position
        self.set_position(self.x_pos + cos(self.direction) * self.speed * Window.delta_time * 50,
                    self.y_pos + sin(self.direction) * self.speed * Window.delta_time * 50)
        
        #check if durtation has passed
        if time() > self.start_time + self.duration:
            self.delete()  

        # check collision with objects
        collision = self.player.collision_manager.check_collision_objects(
            self.x_pos, self.y_pos, self.radius)
        if type(collision) != bool:
            if collision.tag == self.target:
                if collision not in self.hit_objects:
                    collision.take_damage(self.damage)
                    self.penetrate -= 1
                    self.hit_objects.append(collision)
                    if self.penetrate < 0:
                        self.delete()

        # Check for collision with screen edge
        collision = self.player.collision_manager.check_collision_screen(
            self.x_pos, self.y_pos)
        if collision[0]:
            # if horizontal, y vector sign flip
            if collision[1] == 0:
                self.direction = atan2(-sin(self.direction),
                                        cos(self.direction))
            # if vertical, x vector sign flip
            else:
                self.direction = atan2(
                    sin(self.direction), -cos(self.direction))
                
        collision = self.player.collision_manager.check_collision_wall( # if collision with wall
            self.x_pos, self.y_pos, self.radius, return_coords=True)
        if not collision[0]: # if collision with wall 
            if collision[1][0] == 0 or collision[1][0] == 31: # collided with vertical wall
                self.direction = atan2(
                    sin(self.direction), -cos(self.direction))
            else: # collided with horizontal wall
                self.direction = atan2(-sin(self.direction),
                                        cos(self.direction))

