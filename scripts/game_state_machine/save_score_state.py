from game_state_machine.game_base_state import GameBaseState
from string import ascii_uppercase
import json
from Window import Window
import requests



class SaveScoreState(GameBaseState):

    SECRET_KEY = "temporary-key123"
    BASE_URL = "https://louisjohns32.pythonanywhere.com/user/"

    def initialise_state(self):
        pass

    def enter_state(self):
        self.input_dict = {i: False for i in (ascii_uppercase)}
        self.input_dict["backspace"] = False
        self.input_dict["return"] = False
        print(self.input_dict)
        self.name = ""

    def check_switch_states(self):
        pass

    def update_state(self):
        for char in self.input_dict:
            if self.state_manager.input_handler.get_input(char):
                print(char)
                if not self.input_dict[char]:
                    if char == "backspace":
                        print("BACK SPACE")
                        self.name = self.name[:len(self.name)-1]
                    elif char == "return":
                        if len(self.name) > 2:
                            self.save_score()
                        else:
                            self.state_manager.main_canvas.create_text(
                                300, Window.WIDTH/2, text="Name must be 3 characters or longer")
                    elif len(self.name) < 12:
                        self.name += char
                    self.input_dict[char] = True
            else:
                self.input_dict[char] = False

        self.render()

    def exit_state(self):
        pass

    def render(self):
        self.state_manager.main_canvas.delete("del")
        self.state_manager.main_canvas.create_rectangle(
            Window.WIDTH/2-200, 150, Window.WIDTH/2+200, 250, fill="white", tag="del")
        self.state_manager.main_canvas.create_text(
            Window.WIDTH/2, 200, text=self.name, tag="del", font="Arial, 30")
        self.state_manager.main_canvas.create_text(
            Window.WIDTH/2, 100, text="Enter name and press return to save", font="Arial, 30", tag="del")

    def save_score(self):
        r = requests.post(self.BASE_URL + self.name.lower(), json={"secret_key": self.SECRET_KEY, "score":self.score})
        print(r.json)
        self.change_state(self.state_manager.LEADERBOARD)

    def setScore(self, score):
        print("SCORE SET")
        self.score = score