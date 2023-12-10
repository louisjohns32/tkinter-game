from game_state_machine.game_base_state import GameBaseState
from PIL import ImageTk


class BossKeyState(GameBaseState):
    def initialise_state(self):
        # init bosskey image
        self.bosskey_img = ImageTk.PhotoImage(file="assets/boss-key.png")

    def enter_state(self):
        # draw bosskey image
        self.state_manager.main_canvas.create_image(
            1920/2, 1080/2, image=self.bosskey_img, tag="bosskey")

    def exit_state(self):
        # delete bosskey image
        self.state_manager.main_canvas.delete("bosskey")

    def update_state(self):
        pass

    def check_switch_states(self):
        # check for input to exit state
        if self.state_manager.input_handler.get_pressed_combo("control_l", "b"):
            self.change_state(self.state_manager.previous_state)
