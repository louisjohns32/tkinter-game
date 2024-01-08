from game_state_machine.game_base_state import GameBaseState
from PIL import Image, ImageTk
from Window import Window
from string import ascii_uppercase



class InputState(GameBaseState):
    def initialise_state(self):
       pass

    def enter_state(self):
        self.input_dict = {i: False for i in (ascii_uppercase)}
        self.input_dict["backspace"] = False
        self.input_dict["return"] = False
                             

    def check_switch_states(self):
        if not self.sub_state and self.state_manager.input_handler.get_input("return"):
            self.change_state(None)

    def update_state(self):
        for char in self.input_dict:
            if self.state_manager.input_handler.get_input(char):
                if not self.input_dict[char]:
                    if char == "backspace":
                        self.super_state.backspace()
                    
                    else:
                        self.super_state.add_char(char)
                        
                    self.input_dict[char] = True
            else:
                self.input_dict[char] = False

            

    def exit_state(self):
        self.state_manager.main_canvas.delete("del")
        pass

        
        