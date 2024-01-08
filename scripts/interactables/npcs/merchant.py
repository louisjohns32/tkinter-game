from interactables.interactable import Interactable
from player import Player


class Merchant(Interactable):
    idle_anim_args = ["../assets/cyberpunk-pack/merchant.png",(32,36),3]
    idle_anim_kwargs = {"scale":2, "start":6,"time":100}

    items = [1, 2, 3] # list of item ids
    
    def __init__(self, sprite, collision_manager=None, pos=...):
        super().__init__(sprite, collision_manager, pos)
        self.dialogue_tree = {"text": "If you've got the coin, I've got the ware.", "choices":[("What do you have for sale?",
                            lambda: Player.instance.state_manager.current_state.change_state(Player.instance.state_manager.SHOP, self.items )  ),("Did you just... freeze time around us?", {"text":"I like to give my full attention to my interlocutor, and they tend to distract me.",
                            "choices":[("Goodbye", lambda: Player.instance.state_manager.current_state.change_state(Player.instance.state_manager.PLAYING))]}),
                            ( "Goodbye", lambda: Player.instance.state_manager.current_state.change_state(Player.instance.state_manager.PLAYING)) ]}

    
    def on_interact(self):
        # change game state to shop
        Player.instance.state_manager.current_state.change_state(Player.instance.state_manager.DIALOGUE, self.dialogue_tree, self.sprite)

