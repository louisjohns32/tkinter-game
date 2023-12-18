import math
from Window import Window


class collision_manager:

    def __init__(self, MAP_ARRAY, TILE_SIZE, state_manager):
        self.collidable_objects = []
        self.MAP_ARRAY = MAP_ARRAY
        self.TILE_SIZE = TILE_SIZE
        self.state_manager = state_manager

    def check_collision_wall(self, x, y, radius, return_coords=False):
        radius *= Window.SCALE
        # Convert x,y from world coordinates to map coordinates
        x = int(x//self.TILE_SIZE)
        y = int(y//self.TILE_SIZE)

        # check against map_array
        try:
            if str(self.MAP_ARRAY[x][y])[0] == "0":
                if return_coords:
                    return False, (x,y)
                return False
        except: # x,y out of map bounds
            if return_coords:
                return False,(x,y)
            return False
        # Otherwise return true
        if return_coords:
            return True, (x,y)
        return True

    def check_collision_objects(self, x, y, radius, tag=""):
        radius *= Window.SCALE
        res = []
        # check against other objects - can be optimised further in future, instead of looping through all objects
        for obj in self.collidable_objects:

            if abs(obj.x_pos - x) < radius + obj.radius and abs(obj.y_pos - y) < radius + obj.radius:
                # Collision
                if tag == "" or obj.tag == tag:
                    res.append(obj)

        if len(res) == 0:
            return False
        return res

        # TODO Store enemies in each tile, and only check collisions with enemies in adjacent tiles to better optimise

    def check_collision(self, x, y, radius): # checks collision with wall and objects
        if self.check_collision_wall(x, y, radius):
            return self.check_collision_objects(x, y, radius)
        return True

    def check_collision_line(self, x, y, angle=0, width=1):
        width *= Window.SCALE
        # checks collision along line at given angle from x,y with given width
        collided_objs = []
        for obj in self.collidable_objects:
            distance = math.sqrt((obj.x_pos - x)**2 + (obj.y_pos - y)**2)
            if distance == 0:
                distance = 0.00001
            # Maximum angle for this distance such that the object is on the line
            max_ang = math.radians(360)*width/(distance)
            obj_angle = abs(math.atan2(obj.y_pos-y, obj.x_pos-x) - angle)
            if obj_angle < max_ang:
                # COLLISION
                collided_objs.append(obj)
        return collided_objs

    def check_collision_screen(self, x, y):
        # checks collision with screen edges
        # returns bool, int where the int is 0 if the 
        # wall is horizontal, or 1 if vertical
        edges = self.state_manager.PLAYING.camera.get_edges()

        if x < edges[0][0]:
            return True, 1
        elif x > edges[1][0]:
            return True, 1
        elif y < edges[0][1]:
            return True, 0
        elif y > edges[1][1]:
            return True, 0
        return False, -1

    def check_out_of_bounds(self, x, y):
        # Convert x,y from world coordinates to map coordinates
        x = int(x//self.TILE_SIZE)
        y = int(y//self.TILE_SIZE)

        # check if outside of map
        if x < 0 or x > len(self.MAP_ARRAY)-1 or y < 0 or y > len(self.MAP_ARRAY[0])-1:
            return False
        return True
    
    def check_collision_square(self,x,y,radius,tag=""):
        radius *= Window.SCALE
        # check against other objects - can be optimised further in future, instead of looping through all objects
        for obj in self.collidable_objects:
            if obj.tag != tag:
                continue
            # check if within square
                # check if object lies within x-radius x+radius
                if obj.x_pos > x-radius and obj.x_pos < x + radius:
                    # check if object lies within y-radius y+radius
                    if obj.y_pos > y-radius and obj.y_pos < y + radius:
                        #   return collision
                        return obj
                    # if both are true, return collision
            pass
        return False

    def update(self):
        # TODO Reimplement collision detection between enemies
        pass

    def remove_object(self, obj):
        try:
            self.collidable_objects.remove(obj)
        except Exception as e:
            return False
