from game_state_machine.game_base_state import GameBaseState
import json


class OptionsState(GameBaseState):
    def initialise_state(self):
        pass

    def enter_state(self):
        self.selected_option = 0
        # load current binds
        with open("binds.json", "r") as file:
            self.binds_dict = json.load(file)

    def exit_state(self):
        pass

    def update_state(self):
        if self.state_manager.input_handler.get_pressed_action("up"):
            self.selected_option = max(0, self.selected_option - 1)
        elif self.state_manager.input_handler.get_pressed_action("down"):
            self.selected_option = min(
                len(self.binds_dict)-1, self.selected_option + 1)
        self.render()

    def check_switch_states(self):
        if self.state_manager.input_handler.get_pressed_action("back"):
            self.change_state(self.state_manager.MAINMENU)

        elif self.state_manager.input_handler.get_pressed_action("select"):
            self.state_manager.CHANGINGBIND.set_action(
                list(self.binds_dict.keys())[self.selected_option])
            self.change_state(self.state_manager.CHANGINGBIND)

    def render(self):
        self.state_manager.main_canvas.delete("del")
        self.state_manager.main_canvas.create_rectangle(
            200, 200, 1720, 880, fill="white", tag="del")
        for i, bind in enumerate(self.binds_dict):
            if i == self.selected_option:
                color = "blue"
            else:
                color = "black"
            self.state_manager.main_canvas.create_text(
                Window.WIDTH/2, 300 + i*50, font="Arial, 20", text=bind, tag="del")
            self.state_manager.main_canvas.create_text(
                Window.WIDTH/2 + 200, 300 + i*50, font="Arial, 20", text=self.binds_dict[bind], tag="del", fill=color)
