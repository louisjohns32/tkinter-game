from interactables.interactable import Interactable
from player import Player


class SpawnPoint(Interactable):
    def __init__(self, sprite, collision_manager=None, pos=...):
        super().__init__(sprite, collision_manager, pos)

    def on_interact(self):
        if Player.instance.state_manager.current_state.sub_state != Player.instance.state_manager.WAVES:
            Player.instance.state_manager.current_state.enemy_spawner.nextWave()
            Player.instance.state_manager.current_state.change_sub_state(Player.instance.state_manager.WAVES)
        else:
            pass