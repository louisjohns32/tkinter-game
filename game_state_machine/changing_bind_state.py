from game_state_machine.game_base_state import GameBaseState
import json


class ChangingBindState(GameBaseState):
    def initialise_state(self):
        pass

    def enter_state(self):
        # load current binds
        with open("binds.json", "r") as file:
            self.binds_dict = json.load(file)

    def exit_state(self):
        self.binds_dict[self.action] = self.key
        # update binds.json file
        with open("binds.json", "w") as file:
            json.dump(self.binds_dict, file)
        self.state_manager.input_handler.update_bind(self.action, self.key)

    def update_state(self):
        self.render()
        pass

    def check_switch_states(self):
        key = self.state_manager.input_handler.get_key_down()
        if key:
            self.key = key
            self.change_state(self.state_manager.OPTIONS)

    def render(self):
        self.state_manager.main_canvas.delete("del")
        self.state_manager.main_canvas.create_rectangle(
            200, 200, 1720, 880, fill="white", tag="del")
        for i, bind in enumerate(self.binds_dict):
            if bind == self.action:
                self.state_manager.main_canvas.create_text(
                    1920/2 + 200, 300 + i*50, font="Arial, 20", text="Type key to bind", tag="del", fill="blue")
            else:
                self.state_manager.main_canvas.create_text(
                    1920/2 + 200, 300 + i*50, font="Arial, 20", text=self.binds_dict[bind], tag="del")
            self.state_manager.main_canvas.create_text(
                1920/2, 300 + i*50, font="Arial, 20", text=bind, tag="del")

    def set_action(self, action):
        self.action = action
