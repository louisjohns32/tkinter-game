from game_state_machine.game_base_state import GameBaseState
import json
import os
import datetime


class LoadingGameState(GameBaseState):
    def initialise_state(self):
        pass

    def enter_state(self):
        # generates string list of saves
        self.saves = os.listdir("saves")[::-1]
        self.selected = 0

    def check_switch_states(self):
        if self.state_manager.input_handler.get_pressed_action("select"):
            self.save_name = self.saves[self.selected]
            self.change_state(self.state_manager.PLAYING)

    def update_state(self):
        if self.state_manager.input_handler.get_pressed_action("up"):
            self.selected = max(0, self.selected - 1)
        elif self.state_manager.input_handler.get_pressed_action("down"):
            self.selected = min(len(self.saves)-1, self.selected + 1)
        self.render()

    def exit_state(self):
        with open(f"saves/{self.save_name}", "r") as file:
            save_dict = json.load(file)
        self.state_manager.PLAYING.load(save_dict)

    def render(self):
        self.state_manager.main_canvas.delete("del")
        self.state_manager.main_canvas.create_rectangle(
            200, 200, 1720, 880, fill="white", tag="del")

        for i, save in enumerate(self.saves[(self.selected//10)*10:(self.selected//10)*10 + 10]):
            if i + (self.selected//10)*10 == self.selected:
                self.state_manager.main_canvas.create_text(
                    1000, 300 + i*60, text=datetime.datetime.fromtimestamp(int(save.strip(".json")[0:10])), fill="blue", tag="del")
            else:
                self.state_manager.main_canvas.create_text(
                    1000, 300 + i*60, text=datetime.datetime.fromtimestamp(int(save.strip(".json")[0:10])), tag="del")
