from interactable import Interactable
from player import Player


class TalkableNPC(Interactable):
    idle_anim_args = ...

    dialogue_tree ={"text":"Hey there!", "next":None}
    dialogue_active = False

    def __init__(self, sprite, collision_manager=None, pos=...):
        super().__init__(sprite, collision_manager, pos)
        self.current_dialogue = self.dialogue_tree

    def on_interact(self):
        # show dialogue
        self.dialogue_active = True
        self.prompt_active = False
        
    def update(self):
        if not self.dialogue_active: # TODO could use some sort of state machine instead?
            super().update()
        else:
            # check if player outside of range, if so close dialogue
            if (Player.instance.x_pos - self.x_pos)**2 + \
            (Player.instance.y_pos - self.y_pos)**2 >= self.prompt_range**2:
                self.dialogue_active = False
        

    def draw_to_screen(self, pos, canvas):
        super().draw_to_screen(pos, canvas)
        if self.dialogue_active: # TODO could use some sort of state machine instead?
            canvas.create_rectangle(pos[0]+25, pos[1], pos[0]+150, pos[1]-100, fill="white")
            canvas.create_text(pos[0]+92, pos[1]-50, text=self.current_dialogue["text"])


