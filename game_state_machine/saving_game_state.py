from game_state_machine.game_base_state import GameBaseState
import json
from time import time


class SavingGameState(GameBaseState):
    def initialise_state(self):
        pass

    def enter_state(self):
        pass

    def check_switch_states(self):
        self.change_state(self.state_manager.PAUSED)

    def update_state(self):
        pass

    def exit_state(self):
        save_dict = {}

        # Really, all i need to save is all the game objects, I should have a gameObject.save() method which returns the dict to be saved and can be overriden to add more info.

        # Save some meta data about save
        save_dict["meta"] = self.storeMeta()
        # Save player
        save_dict["player"] = self.state_manager.PLAYING.player.save()
        # Save score
        save_dict["score"] = self.state_manager.PLAYING.player_score
        # Save enemy spawner
        save_dict["spawner"] = self.state_manager.PLAYING.enemy_spawner.save()
        # Save all gameobjects
        obj_list = []
        for obj in self.state_manager.PLAYING.obj_manager.game_objects:
            if obj.type != "Player" and obj.type.count("Projectile") == 0:
                obj_list.append(obj.save())
        save_dict["objects"] = obj_list

        # Save to json

        with open(f"saves/{str(time()).replace('.','')}.json", "w") as file:
            json.dump(save_dict, file)

    def storeMeta(self):
        save_dict = {}
        save_dict["time"] = time()
        return save_dict
