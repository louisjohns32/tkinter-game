from game_state_machine.game_base_state import GameBaseState


class WavesState(GameBaseState):
    def initialise_state(self):
        pass

    def enter_state(self):
        pass

    def exit_state(self):
        pass

    def update_state(self):
        self.super_state.enemy_spawner.update()
        pass

    def check_switch_states(self):
        pass
