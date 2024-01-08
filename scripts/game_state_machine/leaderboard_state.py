from game_state_machine.game_base_state import GameBaseState
import json
from math import ceil
import requests


class LeaderBoardState(GameBaseState):
    
    URL = "https://louisjohns32.pythonanywhere.com/scores"

    def initialise_state(self):
        pass

    def enter_state(self):
        self.page = 0

        self.highscores_dict = requests.get(self.URL).json()
        self.highscores_list = sorted(self.highscores_dict.items(), key=lambda x: x[1])[
                ::-1]  # sorts by score, stores tuples (name, score)

        self.max_pages = ceil(len(self.highscores_list)/10)

    def check_switch_states(self):
        if self.state_manager.input_handler.get_input_action("back"):
            self.change_state(self.state_manager.MAINMENU)

    def update_state(self):
        self.render()

        if self.state_manager.input_handler.get_pressed_action("right"):
            self.page = min(self.page+1, self.max_pages-1)
        if self.state_manager.input_handler.get_pressed_action("left"):
            self.page = max(0, self.page - 1)

    def exit_state(self):
        self.state_manager.main_canvas.delete("del")
        pass

    def render(self):
        self.state_manager.main_canvas.delete("del")
        self.state_manager.main_canvas.create_rectangle(
            200, 200, 1720, 880, fill="white", tag="del")

        for i, (name, score) in enumerate(self.highscores_list[self.page*10:self.page*10 + 10]):
            self.state_manager.main_canvas.create_text(
                1000, 300 + i*60, text=f"{i + 1 + self.page*10} - {name} - score: {score}", tag="del")
