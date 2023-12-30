from game_state_machine.game_base_state import GameBaseState
from PIL import ImageTk, Image
from time import time
from game_state_machine.boss_state import BossState
from Window import Window
from player import Player


class DialogueState(GameBaseState):

    def initialise_state(self): # TODO resize
        self.selected_choice_sprite = ( 
            Image.open("assets/buttonHighLight.png"))
        self.selected_choice_sprite = ImageTk.PhotoImage(self.selected_choice_sprite.resize((
            int(self.selected_choice_sprite.width*Window.SCALE * 2),int(self.selected_choice_sprite.height*Window.SCALE))))

        self.choice_sprite = ( 
            Image.open("assets/buttonNormal.png"))
        self.choice_sprite = ImageTk.PhotoImage(self.choice_sprite.resize((
            int(self.choice_sprite.width*Window.SCALE * 2),int(self.choice_sprite.height*Window.SCALE))))
        

    def enter_state(self, dialogue_tree, sprite):
        self.start_time = time()
        self.npc_sprite = sprite
        self.dialogue_tree = dialogue_tree

        self.selected_option = 0

        self.current_dialogue = self.dialogue_tree
        self.choices = self.current_dialogue["choices"]

    def check_switch_states(self):

        pass

    def update_state(self):
        if self.state_manager.input_handler.get_pressed_action("up"):
            self.selected_option = max(0, self.selected_option - 1)
        elif self.state_manager.input_handler.get_pressed_action("down"):
            self.selected_option = min(
                len(self.choices)-1, self.selected_option + 1)
            
        if self.state_manager.input_handler.get_pressed_action("select"):
            # change current dialogue or execute function
            if type(self.choices[self.selected_option][1]) == dict:
                self.current_dialogue = self.choices[self.selected_option][1]
                self.choices = self.current_dialogue["choices"]
            else:
                self.choices[self.selected_option][1]()
                

        self.render()

    def exit_state(self):
        self.state_manager.PLAYING.enemy_spawner.start_time += (
            time() - self.start_time)
        pass

    def render(self):
        self.state_manager.main_canvas.delete("del")
        # draw npc sprite

        # draw text box

        # draw npc text
        self.state_manager.main_canvas.create_text(Window.WIDTH/2, 200, text=self.current_dialogue["text"], tag="del", font=("Arial", 30))

        for i,choice in enumerate(self.choices):
            if i == self.selected_option:
                self.state_manager.main_canvas.create_image(
                    950*Window.SCALE, (600 + i*150)*Window.SCALE, image=self.selected_choice_sprite, tag="del")
                self.state_manager.main_canvas.create_text(
                    950*Window.SCALE, (605 + i*150)*Window.SCALE, text=choice[0], font=("Arial", int(30*Window.SCALE)), tag="del", fill="white")
            else:
                self.state_manager.main_canvas.create_image(
                    950*Window.SCALE, (600 + i*150)*Window.SCALE, image=self.choice_sprite, tag="del")
                self.state_manager.main_canvas.create_text(
                    950*Window.SCALE, (605 + i*150)*Window.SCALE, text=choice[0], font=("Arial", int(30*Window.SCALE)), tag="del", fill="white")