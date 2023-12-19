from player import Player
from game_object import GameObject
from enemies.slime import Slime
from enemies.skeleton import Skeleton
from enemies.rat import Rat
from enemies.flower import Flower
from enemies.dragon_boss import DragonBoss
from enemies.boss import Boss
from projectiles.projectile import Projectile
from projectiles.pinger_projectile import PingerProjectile
from projectiles.orbitor_projectile import OrbitorProjectile
from projectiles.laser_projectile import LaserProjectile


class ObjectManager:

    object_map = {
        "Player": Player,
        "GameObject": GameObject,
        "Slime": Slime,
        "Skeleton": Skeleton,
        "Rat": Rat,
        "Flower": Flower,
        "Dragon": DragonBoss,
        "Boss": Boss,
        "Projectile": Projectile,
        "PingerProjectile": PingerProjectile,
        "OrbitorProjectile": OrbitorProjectile,
        "LaserProjectile": LaserProjectile,
    }

    def __init__(self, collision_manager, objects=[]):
        self.game_objects = []
        # add current objects passed in
        for i in objects:
            self.game_objects.append(i)
        # set references
        self.collision_manager = collision_manager

    def new_object(self, obj,front=False):
        if front:
            # add object to front of list
            self.game_objects.insert(0,obj)
        else:
            self.game_objects.append(obj)
            
        # add to collision manager, if object is collidable
        if obj.collidable:
            self.collision_manager.collidable_objects.append(obj)

    def delete_object(self, obj):
        try:
            self.game_objects.remove(obj)
            obj.awake = False
            # remove from collision manager, if collidable
            if obj.collidable:
                self.collision_manager.collidable_objects.remove(obj)
        except:
            pass # prevents game from crashing in case of bug

    def nuke(self): # delete all objects
        for obj in self.game_objects:
            if obj.tag == "enemy":
                obj.die()
