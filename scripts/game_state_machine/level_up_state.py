from game_state_machine.game_base_state import GameBaseState
from items.wand import Wand
from items.orbitors import Orbitors
from items.shotgun import Shotgun
from items.laser import Laser
from items.pinger import Pinger
from items.shuriken import Shuriken
import random as rand


class LevelUpState(GameBaseState):
    def initialise_state(self):
        print("initialising levelup")
        self.ITEMS = [Wand, Orbitors, Shotgun, Laser, Pinger, Shuriken]

    def enter_state(self):  # called once on state entry
        # pick three random items

        self.items = self.randomItems()
        self.selected_item = 1
        self.count = 100

    def update_state(self):  # called every frame - contains general code
        self.count += 1

        if self.state_manager.input_handler.get_input_action("left") and self.selected_item > 0 and self.count > 5:
            self.selected_item -= 1
            self.count = 0
        if self.state_manager.input_handler.get_input_action("right") and self.selected_item < 2 and self.count > 5:
            self.selected_item += 1
            self.count = 0

        self.render()

    def check_switch_states(self):
        if self.state_manager.input_handler.get_input_action("select"):
            self.change_state(self.state_manager.PLAYING)

    def exit_state(self):  # called once on exit from state
        # TODO This is a bit messy, fix maybe?
        # TODO SUPER MESSY, CHANGE THIS CODE
        if type(self.items[self.selected_item]) == type(str):
            self.ITEMS[self.ITEMS.index(self.items[self.selected_item])] = self.state_manager.PLAYING.player.addItem(
                self.items[self.selected_item])
        else:
            self.ITEMS[self.ITEMS.index(self.items[self.selected_item])] = self.state_manager.PLAYING.player.addItem(
                type(self.items[self.selected_item]))

    def randomItems(self):
        # TODO
        items = []
        player_items = []
        for item in self.ITEMS:
            if type(item) != type(str):  # TODO CHANGE THIS!
                player_items.append(item)

        # pick 1 which the player already has and can lvl up, and 2 new ones
        if player_items != []:
            items.append(player_items[rand.randint(0, 0)])
        else:
            for _ in range(3):
                item = self.ITEMS[rand.randint(0, len(self.ITEMS)-1)]
                while item in items:  # TODO Change this
                    item = self.ITEMS[rand.randint(0, len(self.ITEMS)-1)]
                items.append(item)
            return items
        item = self.ITEMS[rand.randint(0, len(self.ITEMS)-1)]
        while item in items:  # TODO Change this
            item = self.ITEMS[rand.randint(0, len(self.ITEMS)-1)]
        items.append(item)

        if len(player_items) < len(self.ITEMS) - 1:  # 2+ new items can be acquired
            item = self.ITEMS[rand.randint(0, len(self.ITEMS)-1)]
            while item in items:  # TODO Change this
                item = self.ITEMS[rand.randint(0, len(self.ITEMS)-1)]
            items.append(item)

        elif len(player_items) == len(self.ITEMS) - 1:
            item = self.ITEMS[rand.randint(0, len(self.ITEMS)-1)]
            while item in items:  # TODO Change this
                item = self.ITEMS[rand.randint(0, len(self.ITEMS)-1)]
            items.append(item)
            items.append(player_items[rand.randint(0, len(player_items)-1)])
        else:
            items.append(player_items[rand.randint(0, len(player_items)-1)])
            items.append(player_items[rand.randint(0, len(player_items)-1)])

        print(items)
        return items

    def render(self):
        canvas = self.state_manager.main_canvas
        # only delete graohics created in this state to maintain background
        canvas.delete("LevelUpState")
        # TODO get rid of magic numbers
        canvas.create_rectangle(200, 200, 1720, 800, fill="white")
        for i, item in enumerate(self.items):
            if i == self.selected_item:
                color = "blue"
            else:
                color = "black"

            canvas.create_text((i*400 + 300 + 100, 500),
                               fill=color, text=item.name, tag="LevelUpState")
            # TODO SUPER MESSY FIX
            if type(item) != type(str):  # if type(item) is not a type (very meta i know)
                canvas.create_text((i*400 + 300 + 100, 600), fill=color,
                                   text=f"Upgrade to level: {item.level + 1}", tag="LevelUpState")

    def load(self, player_items):
        for player_item in player_items:  # {Item : Level}
            for i, itemtype in enumerate(self.ITEMS):
                if itemtype == type(player_item):
                    self.ITEMS[i] = player_item
