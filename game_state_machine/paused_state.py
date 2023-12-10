from game_state_machine.game_base_state import GameBaseState
from PIL import ImageTk
from time import time
from game_state_machine.boss_state import BossState

class PausedState(GameBaseState):

    def initialise_state(self):
        self.btn_highlighted = ImageTk.PhotoImage(
            file="assets/buttonHighLight.png")
        self.btn_normal = ImageTk.PhotoImage(file="assets/buttonNormal.png")

    def enter_state(self):
        self.selected_option = 0
        self.start_time = time()
        # if in boss fight, remove save button
        if type(self.state_manager.previous_state.sub_state) == BossState:
            self.buttons = [("Continue", lambda: self.change_state(self.state_manager.PLAYING)),  ("Return to menu", lambda: self.change_state(self.state_manager.MAINMENU))]
        else:
            self.buttons = [("Continue", lambda: self.change_state(self.state_manager.PLAYING)), ("Save game",
                                                                  lambda: self.change_state(self.state_manager.SAVINGGAME)),
                                                                    ("Return to menu", lambda: self.change_state(self.state_manager.MAINMENU))]

    def check_switch_states(self):
        if self.state_manager.input_handler.get_pressed_action("select"):
            self.buttons[self.selected_option][1]()

    def update_state(self):
        if self.state_manager.input_handler.get_pressed_action("up"):
            self.selected_option = max(0, self.selected_option - 1)
        elif self.state_manager.input_handler.get_pressed_action("down"):
            self.selected_option = min(
                len(self.buttons)-1, self.selected_option + 1)
        self.render()

    def exit_state(self):
        self.state_manager.PLAYING.enemy_spawner.start_time += (
            time() - self.start_time)
        pass

    def render(self):
        self.state_manager.main_canvas.delete("del")

        for i, btn in enumerate(self.buttons):
            if i == self.selected_option:
                self.state_manager.main_canvas.create_image(
                    950, 600 + i*150, image=self.btn_highlighted, tag="del")
                self.state_manager.main_canvas.create_text(
                    950, 605 + i*150, text=btn[0], font="Arial, 30", tag="del", fill="white")
            else:
                self.state_manager.main_canvas.create_image(
                    950, 600 + i*150, image=self.btn_normal, tag="del")
                self.state_manager.main_canvas.create_text(
                    950, 605 + i*150, text=btn[0], font="Arial, 30", tag="del", fill="white")
