from PIL import Image, ImageTk


class GameObject:  # Should this be abstract? 
    x_pos = 0
    y_pos = 0
    collidable = False
    radius = 16
    tag = ""
    type = "GameObject"

    def __init__(self, sprite, collision_manager=None, pos=(0, 0)):
        self.sprite = sprite
        self.x_pos, self.y_pos = pos
        if collision_manager != None:
            self.collidable = True
        self.collision_manager = collision_manager

        self.awake = True


    def update(self):
        pass

    def set_position(self, x, y):
        if self.collidable:
            if self.collision_manager.check_collision_wall(x, y, self.radius):
                self.x_pos, self.y_pos = x, y
        else:
            self.x_pos, self.y_pos = x, y

    def get_sprite(self):
        return self.sprite, "center"

    def save(self):
        save_dict = {"position": (self.x_pos, self.y_pos)}
        save_dict["type"] = self.type
        save_dict["collidable"] = self.collidable
        return save_dict

    def load(self, info):
        self.x_pos, self.y_pos = info["position"]
