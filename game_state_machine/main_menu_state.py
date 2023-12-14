from game_state_machine.game_base_state import GameBaseState
from PIL import Image, ImageTk
from Window import Window


class MainMenuState(GameBaseState):
    def initialise_state(self):
        # (Name, State to switch to)
        self.options = [("Start", lambda: self.change_state(self.state_manager.PLAYING)), ("Leaderboard",lambda: self.change_state(self.state_manager.LEADERBOARD)),
                         ("Load", lambda: self.change_state(self.state_manager.LOADINGGAME)),
                        ("Options", lambda: self.change_state(self.state_manager.OPTIONS)), ("Quit", lambda: quit())]
        self.selected_option = 0  # index of self.options which is currently selected

    def enter_state(self):
        # draw background
        self.bg = ImageTk.PhotoImage(Image.open(
            "assets/menu-bg.jpg").resize((Window.WIDTH, Window.HEIGHT)))
        self.state_manager.main_canvas.create_image(
            Window.WIDTH/2, Window.HEIGHT/2, image=self.bg)

        # Reset game
        self.state_manager.PLAYING.reset()
        self.state_manager.LEVELUP.reset()

    def check_switch_states(self):
        if self.state_manager.input_handler.get_pressed_action("select"):
            self.options[self.selected_option][1]()

    def update_state(self):
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

        # Render tooltip
        canvas.create_text(1600, 900,
                           text=f'Use {self.state_manager.input_handler.binds_dict["up"]},{self.state_manager.input_handler.binds_dict["left"]},{self.state_manager.input_handler.binds_dict["down"]}, {self.state_manager.input_handler.binds_dict["right"]} to navigate menus',
                           font="Arial, 20", fill="white")
        canvas.create_text(
            1600, 925, text=f'and {self.state_manager.input_handler.binds_dict["select"]} to select ', font="Arial, 20", fill="white")

        # loop through other buttons, adding them ontop or below selected option
        for i, btn in enumerate(self.options):
            if i == self.selected_option:
                canvas.create_text(
                    200, 800 + i*50, text=btn[0],  fill="blue", font=("Arial", 50), tag="del")
            else:
                canvas.create_text(
                    200, 800 + i * 50, text=btn[0],  fill="black", font=("Arial", 20), tag="del")
