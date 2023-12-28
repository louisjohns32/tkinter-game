from string import ascii_lowercase
import json


class InputHandler(object):
    instance = None

    # keysymbol -> bool : true if down, false otherwise
    input_dict = {i: False for i in ascii_lowercase}
    input_dict["space"] = False
    input_dict["backspace"] = False
    input_dict["return"] = False
    input_dict["escape"] = False
    input_dict["control_l"] = False

    # action -> bool : true if key related to action is down, false otherwise
    input_action_dict = {
        "up": False,
        "down": False,
        "right": False,
        "left": False,
        "select": False,
        "pause": False,
        "back": False
    }

    def __init__(self):
        InputHandler.instance = self

        # load input dict
        with open("binds.json", "r") as file:
            binds_dict = json.load(file)
            self.binds_dict_by_key = {}
            for i in binds_dict:
                # within input handler, we need to search the map by key aswell.
                self.binds_dict_by_key[binds_dict[i]] = i
            self.binds_dict = binds_dict
            self.mouse_pos = (0, 0)

    def send_input(self, event): 
        self.input_dict[event.keysym.lower()] = True
        try:
            self.input_action_dict[self.binds_dict_by_key[event.keysym.lower(
            )]] = True
        except:
            pass

    def reset_input(self, event):
        self.input_dict[event.keysym.lower()] = False
        try:
            self.input_action_dict[self.binds_dict_by_key[event.keysym.lower(
            )]] = False
        except:
            pass

    def get_input(self, key):  # True any time its called when the key is held down
        return self.input_dict[key.lower()]

    def get_key_down(self):  # returns first key down or false if none are down
        for key in self.input_dict:
            if self.input_dict[key]:
                return key
        return False

    def get_pressed_combo(self, key1, key2): # get key combo i.e. ctrl + z
        return_val = self.input_dict[key1.lower(
        )] and self.input_dict[key2.lower()]
        if return_val:
            self.input_dict[key1.lower()] = False
            self.input_dict[key2.lower()] = False
        return return_val

    def get_mouse_pos(self): # returns mouse position in screen coordinates
        return self.mouse_pos

    def set_mouse_pos(self, event):
        self.mouse_pos = (event.x, event.y)

    def get_pressed(self, key):  # Only true once, when it is called
        return_val = self.input_dict[key.lower()]
        self.input_dict[key.lower()] = False
        return return_val

    def get_input_action(self, action):
        return self.input_action_dict[action]

    def get_pressed_action(self, action):
        return_val = self.input_action_dict[action]
        self.input_action_dict[action] = False
        self.input_dict[self.binds_dict[action]] = False
        return return_val

    def update_bind(self, action, key):
        del self.binds_dict_by_key[self.binds_dict[action]]
        self.binds_dict[action] = key
        self.binds_dict_by_key[key] = action
