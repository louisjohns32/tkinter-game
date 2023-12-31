from tkinter import Tk, ttk, Canvas
from managers.input_handler import InputHandler
from game_state_machine.game_state_manager import GameStateManager
from managers.map_manager import MapManager
from Window import Window
from math import sqrt
from time import time
import requests


# Should player be a game object (Player inherrits GameObject), or its own thing?

# CREDITS/CITATIONS:
# Stone wall: https://opengameart.org/content/handpainted-stone-wall-textures
# Grass block: https://opengameart.org
# Player spritesheet: https://opengameart.org/content/3-cyberpunk-characters
# Slime spritesheet:https://opengameart.org
# Skeleton spritesheet:https://opengameart.org/content/skeleton-guy-animated
# Rat spritesheet:https://opengameart.org
# Flower spritesheet:https://opengameart.org/content/lpc-monsters
# Dragon spritesheet:https://opengameart.org/content/flying-dragon-rework
# Dragon firebreath: https://opengameart.org/content/9-frame-fire-animation-16x-32x-64x
# Paused buttons: https://opengameart.org/content/fantasy-ui-button
# Menu background: generated by me with AI using https://pixlr.com/
# Orbitors projectile spritesheet: https://opengameart.org/content/evil-blood-orb-animated

    

def main():
    # create and configure root winroot = Tk()
    global input_handler, main_canvas, root
    root = Tk()
    root.attributes("-fullscreen", True)
    root.resizable(width=False, height=False)
    WIDTH = root.winfo_screenwidth()
    HEIGHT = root.winfo_screenheight()
    SCALE = sqrt((WIDTH*HEIGHT)/(1920*1080))

    window = Window()
    Window.HEIGHT = HEIGHT
    Window.WIDTH = WIDTH
    Window.SCALE = SCALE

        # create and configure canvas
    main_canvas = Canvas(root, width=WIDTH, height=HEIGHT, bg="white")
    main_canvas.pack(side="right")

        # initialise input handler
    input_handler = InputHandler()
    root.bind("<KeyPress>", input_handler.send_input)
    root.bind("<KeyRelease>", input_handler.reset_input)
    root.bind("<Motion>", input_handler.set_mouse_pos)

    root.update()
    start_game()


def start_game():
    global state_manager, window, start_time
    start_time = time()
    
    map_manager = MapManager()
    state_manager = GameStateManager(
        map_manager=map_manager, input_handler=input_handler, main_canvas=main_canvas)

    
    

    game_loop()

def game_loop():
    global start_time
    while True:
        Window.delta_time = time() - start_time
        start_time = time()
        state_manager.update()

        root.update_idletasks()
        root.update()
if __name__ == "__main__":
     main()




