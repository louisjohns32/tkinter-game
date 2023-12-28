from abc import abstractmethod
from game_object import GameObject
from player import Player
from PIL import Image, ImageTk
from Window import Window
from input_handler import InputHandler


class Interactable(GameObject):    
    prompt_range = 200
    prompt_sprite_path = "assets/e-prompt.png"           # TODO use a prompt dict to choose prompt based on action, rather than key
                                        # to allow user to remap interact key and for the prompt to reflect that
    

    def __init__(self, sprite, collision_manager=None, pos=...):
        super().__init__(sprite, collision_manager, pos)
        self.prompt_active = False
        self.prompt_range = self.prompt_range

        self.prompt_sprite = ImageTk.PhotoImage(Image.open(self.prompt_sprite_path).resize((int(46*Window.SCALE)
                                                                                           , int(46*Window.SCALE))))

    @abstractmethod
    def on_interact(self):
        pass

    def update(self):
        # check if player in prompt range
        if (Player.instance.x_pos - self.x_pos)**2 + \
        (Player.instance.y_pos - self.y_pos)**2 < self.prompt_range**2:
            self.prompt_active = True
            if InputHandler.instance.get_input("e"):
                self.on_interact()
        else:
            self.prompt_active = False
    
    def draw_to_screen(self, pos, canvas):
        super().draw_to_screen(pos,canvas)

        # draw prompt menu
        if self.prompt_active:
            canvas.create_image(pos[0],pos[1]-50, image=self.prompt_sprite)

