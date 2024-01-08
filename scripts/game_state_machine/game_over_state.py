from game_state_machine.game_base_state import GameBaseState
from PIL import ImageTk


class GameOverState(GameBaseState):

    def initialise_state(self):
        self.buttons = [("Save Score", lambda: self.change_state(self.state_manager.SAVESCORE)), ("Play again",
                                                                      lambda: self.change_state(self.state_manager.PLAYING)),
                                                                        ("Return to menu", lambda: self.change_state(self.state_manager.MAINMENU))]
        self.btn_highlighted = ImageTk.PhotoImage(
            file="../assets/buttonHighLight.png")
        self.btn_normal = ImageTk.PhotoImage(file="../assets/buttonNormal.png")

    def enter_state(self):
        print("Entered GAMEOVER")
        self.selected_option = 0

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
        print("Exiting gameover")
        self.state_manager.SAVESCORE.setScore(
            self.state_manager.PLAYING.player_score)
        self.state_manager.PLAYING.reset()
        self.state_manager.LEVELUP.reset()

    def render(self):
        self.state_manager.main_canvas.delete("del")
        self.state_manager.main_canvas.create_rectangle(
            400, 200, 1520, 480, fill="black", tag="del")
        self.state_manager.main_canvas.create_text(
            950, 340, text="YOU DIED", fill="red", font="Arial, 50", tag="del")

        for i, btn in enumerate(self.buttons):
            if i == self.selected_option:
                self.state_manager.main_canvas.create_image(
                    950, 600 + i*150, image=self.btn_highlighted, tag="del")
            else:
                self.state_manager.main_canvas.create_image(
                    950, 600 + i*150, image=self.btn_normal, tag="del")
            self.state_manager.main_canvas.create_text(
                950, 605 + i*150, text=btn[0], font="Arial, 30", tag="del", fill="white")
