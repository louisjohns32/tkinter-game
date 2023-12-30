from game_state_machine.game_base_state import GameBaseState
from PIL import ImageTk, Image
from time import time
from game_state_machine.boss_state import BossState
from Window import Window
from items.item_manager import ItemManager


class ShopState(GameBaseState):

    def initialise_state(self): # TODO resize
        # initialise sprites
        pass
        

    def enter_state(self, items): # list of item ids      
        self.items = items
        self.selected_item = 0

        self.start_time = time()

    def check_switch_states(self):
        pass            


    def update_state(self):
        if self.state_manager.input_handler.get_pressed_action("left"):
            self.selected_item = max(0, self.selected_item - 1)
        elif self.state_manager.input_handler.get_pressed_action("right"):
            self.selected_item = min(
                len(self.items)-1, self.selected_item + 1)
        
        if self.state_manager.input_handler.get_pressed_action("down"):
            self.selected_item = 4
            
        if self.state_manager.input_handler.get_pressed_action("select"):
            if self.selected_item == 4:
                self.change_state(self.state_manager.PLAYING)
            else:
                # check if player already has item, if they do upgrade the weapon, otherwise give them the weapon
                pass

        self.render()


    def exit_state(self):
        self.state_manager.PLAYING.enemy_spawner.start_time += (
            time() - self.start_time)
        pass

    def render(self):
        self.state_manager.main_canvas.delete("del")
        
        # render background
        self.state_manager.main_canvas.create_rectangle(Window.WIDTH/8, Window.HEIGHT/8, 7*Window.WIDTH/8, 7*Window.HEIGHT/8, fill="darkgoldenrod")

        for i,item in enumerate(self.items):
            kwargs = {"fill":"sandybrown"}
            if i == self.selected_item:
                kwargs["outline"] = "white"
                kwargs["width"] = 10
                
            self.state_manager.main_canvas.create_rectangle((Window.WIDTH/4)*(i+1)-150, Window.HEIGHT/4, (Window.WIDTH/4)*(i+1)+150, 3*Window.HEIGHT/4, **kwargs, tag="del")    
            #self.state_manager.main_canvas.create_image(...)
            self.state_manager.main_canvas.create_text((Window.WIDTH/4)*(i+1),Window.HEIGHT/2, text=ItemManager.items_id_dict[item].name)

        # draw exit button
        kwargs = {}
        if self.selected_item == 4:
            kwargs["outline"] = "white"
            kwargs["width"] = 10

        # self.state_manager.create_rectangle(...)
        # self.state_manager.create_text(..., text="Exit")


         
