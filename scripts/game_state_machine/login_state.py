from game_state_machine.game_base_state import GameBaseState
from PIL import Image, ImageTk
from Window import Window
import requests


class LoginState(GameBaseState):
    def initialise_state(self):
        # (Name, State to switch to)
        self.options = [("Username", lambda : self.change_sub_state(self.state_manager.INPUT)), ("Password", lambda : self.change_sub_state(self.state_manager.INPUT)),("Login", lambda:self.login()),("Back", lambda:self.change_state(self.state_manager.MAINMENU))]
        self.selected_option = 0  # index of self.options which is currently selected

    def enter_state(self):
        self.input_fields = {"username":"", "password": ""}
                             

    def check_switch_states(self):
        if not self.sub_state and self.state_manager.input_handler.get_pressed_action("select"):
            self.options[self.selected_option][1]()

    def update_state(self):
        if not self.sub_state:
            if self.state_manager.input_handler.get_pressed_action("up"):
                self.selected_option = max(0, self.selected_option - 1)
            elif self.state_manager.input_handler.get_pressed_action("down"):
               self.selected_option = min(
                  len(self.options)-1, self.selected_option + 1)
            
        self.render()

    def exit_state(self):
        self.state_manager.main_canvas.delete("del")
        pass

    def render(self):
        canvas = self.state_manager.main_canvas
        canvas.delete("del")

        for i,input_field in enumerate(self.input_fields):
            canvas.create_rectangle(Window.WIDTH/2-100*Window.SCALE, Window.HEIGHT/2 + 200 * i * Window.SCALE,
                                     Window.WIDTH/2+100*Window.SCALE, Window.HEIGHT/2 + 200 * i * Window.SCALE - 100 * Window.SCALE,
                                       fill="white", outline="blue" if i == self.selected_option else "black", width=2 , tag="del")
            canvas.create_text(Window.WIDTH/2-100*Window.SCALE, Window.HEIGHT/2 + 200 * i * Window.SCALE, text=self.input_fields[input_field] if self.input_fields[input_field] else input_field, tag="del")


    def backspace(self):
        field_value =  self.input_fields[self.options[self.selected_option][0].lower()]
        self.input_fields[self.options[self.selected_option][0].lower()] = field_value[0: len(field_value)-1]

    def add_char(self, char):
        if char == "return":
            return
        if len(self.input_fields[self.options[self.selected_option][0].lower()]) < 12:
            self.input_fields[self.options[self.selected_option][0].lower()] += char

    
    def login(self):
        # compare with sql database
        login_successful = True

        if login_successful:
            self.state_manager.main_canvas.create_text(Window.WIDTH/2, Window.HEIGHT - 50 * Window.SCALE, text="Logged in!")
            self.change_state(self.state_manager.MAINMENU)
        
        else:
            self.state_manager.main_canvas.create_text(Window.WIDTH/2, Window.HEIGHT - 50 * Window.SCALE, text="Username or password incorrect.")
        


        
        