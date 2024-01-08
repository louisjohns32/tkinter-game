from abc import ABC, abstractmethod
from player import Player


class DumbObject(ABC):
    instance = None
    max_items = 20
    def __init__(self):
        type(self).instance = self
        self.player = Player.instance
        self.obj_list = []

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def draw_to_screen(self, canvas):
        pass

    def add_object(self, *args):
        self.obj_list.append(args[0])
        if len(self.obj_list) > self.max_items:
            self.obj_list.pop(0)