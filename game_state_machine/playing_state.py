from game_state_machine.game_base_state import GameBaseState
from camera import Camera
from collision_manager import collision_manager
from object_manager import ObjectManager
from player import Player
from enemy_spawner import enemy_spawner
from PIL import Image, ImageTk
from time import time
import math
from game_object import GameObject
from Window import Window

class PlayingState(GameBaseState):
    # Not using init as this is called when the state is reset, instead of a new instance being used
    def initialise_state(self):
        print("initialising playing state")
        self.camera = Camera()
        self.collision_manager = collision_manager(
            self.state_manager.map_manager.MAP_ARRAY, self.state_manager.map_manager.TILE_SIZE, self.state_manager)
        self.obj_manager = ObjectManager(self.collision_manager)
        print(f"Game objects after init: {self.obj_manager.game_objects}")
        self.player = Player(self.state_manager.input_handler,  ImageTk.PhotoImage
                             (file="cowboy.png"), self.collision_manager, self.obj_manager, self.state_manager)
        self.enemy_spawner = enemy_spawner(time(), self.obj_manager, self.player)
        self.obj_manager.new_object(self.player)
        self.delta_time = 0
        self.change_sub_state(self.state_manager.WAVES)
        print("SCORE RESET")
        self.player_score = 0

    def enter_state(self):
        self.start_time = time()

    def exit_state(self):
        pass

    def update_state(self):

        self.delta_time = time() - self.start_time
        self.start_time = time()
        for obj in self.obj_manager.game_objects:  # loop through all gameobjects and call update on each

            obj.update()

        self.collision_manager.update()
        self.camera.update()

        self.render()

        # cheatcodes
        if self.state_manager.input_handler.get_pressed_combo("f","q"):
            self.obj_manager.nuke() # kill all enemies
        
        if self.state_manager.input_handler.get_pressed_combo("control_l", "h"):
            self.player.increase_health(10000) # reset health

    def check_switch_states(self):
        if self.player.leveled:
            self.player.leveled = False
            self.change_state(self.state_manager.LEVELUP)
        if self.state_manager.input_handler.get_input_action("pause"):

            self.change_state(self.state_manager.PAUSED)

    def render(self):
        # TODO add different layers and only delete layers which need updating
        self.state_manager.main_canvas.delete("all")
        if self.collision_manager.check_out_of_bounds(self.player.x_pos-Window.WIDTH/2, self.player.y_pos) and self.collision_manager.check_out_of_bounds(self.player.x_pos+Window.WIDTH/2, self.player.y_pos):
            self.camera.set_position(self.player.x_pos, self.camera.y_pos)
        if self.collision_manager.check_out_of_bounds(self.player.x_pos, self.player.y_pos+Window.HEIGHT/2) and self.collision_manager.check_out_of_bounds(self.player.x_pos, self.player.y_pos-Window.HEIGHT/2):
            self.camera.set_position(self.camera.x_pos, self.player.y_pos)
        # draw all graphics to screen
        # draw tile map
        # TODO Change to loop through tiles in camera frame alone
        for x, tile_row in enumerate(self.state_manager.map_manager.MAP_ARRAY):
            for y, tile in enumerate(tile_row):
                self.state_manager.main_canvas.create_image(x*self.state_manager.map_manager.TILE_SIZE-self.camera.x_pos + 8*self.state_manager.map_manager.TILE_SIZE,
                                                          y * self.state_manager.map_manager.TILE_SIZE - self.camera.y_pos + 5*self.state_manager.map_manager.TILE_SIZE, image=self.state_manager.map_manager.TEXTURE_MAP[self.state_manager.map_manager.MAP_ARRAY[x][y]])
        # draw game objects
        for obj in self.obj_manager.game_objects:
            # get position in world
            x = obj.x_pos
            y = obj.y_pos
            # get position relative to camera
            x = x-self.camera.x_pos
            y = y-self.camera.y_pos
            # get position on screen
            x += (Window.WIDTH/2)  # TODO URGENT GET RID OF MAGIC NUMBERS
            y += (Window.HEIGHT/2)
            # get sprite
            sprite = obj.get_sprite()[0]
            # get anchoring
            anchor = obj.get_sprite()[1]  # default is center
            if anchor == "left":
                x += sprite.width()//2
            elif anchor == "right":
                x -= sprite.width()//2
            elif anchor == "player":
                angle = math.atan2(obj.y_pos - self.player.y_pos,
                                   obj.x_pos - self.player.x_pos)
                length = math.sqrt(sprite.width()**2 + sprite.height()**2)

                x += math.cos(angle) * length/2
                y += math.sin(angle) * length/2
            # draw sprite if on screen
            self.state_manager.main_canvas.create_image(
                x, y, image=obj.get_sprite()[0])

        # Render healthbar
        self.state_manager.main_canvas.create_rectangle(
            Window.WIDTH/2-100, 940, Window.WIDTH/2 + 100, 1040, fill="black")
        self.state_manager.main_canvas.create_rectangle(
            Window.WIDTH/2-100, 940, (Window.WIDTH/2 - 100 + 200*(self.player.health/self.player.max_health)), 1040, fill="red")
        # Render xp bar
        self.state_manager.main_canvas.create_rectangle(
            Window.WIDTH/2-400, 1040, Window.WIDTH/2 + 400, Window.HEIGHT, fill="black")
        self.state_manager.main_canvas.create_rectangle(
            Window.WIDTH/2-400, 1040, (Window.WIDTH/2 - 400 + 800*(self.player.xp/self.player.max_xp)), Window.HEIGHT, fill="blue")
        self.state_manager.main_canvas.create_text(
            Window.WIDTH/2-300, 1060, text=f"Level: {self.player.level}", fill="white", font=("Arial", 20))
        # Render score
        self.state_manager.main_canvas.create_text(
            100, 50, text=f"Score: {self.player_score}", fill="white", font=("Arial", 24))

    def addScore(self, amnt):
        self.player_score += amnt

    def load(self, save_dict):
        # Load player
        self.player.load(save_dict["player"])
        # Load enemy spawner
        self.enemy_spawner.load(save_dict["spawner"], save_dict["meta"]["time"])
        # Load levelupstate
        self.state_manager.LEVELUP.load(self.player.items)
        # Load score
        self.player_score = save_dict["score"]
        # Load gameobjects
        for obj_info in save_dict["objects"]:
        
            if self.obj_manager.object_map[obj_info["type"]] == GameObject:
                print("AA")
                continue
            obj = self.obj_manager.object_map[obj_info["type"]](ImageTk.PhotoImage(
                file="testObj.png"), self.player, collision_manager=self.collision_manager)

            obj.load(obj_info)
            self.obj_manager.new_object(obj)
