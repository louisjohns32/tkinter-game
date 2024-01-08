from abc import ABC, abstractmethod


class GameBaseState(ABC):
    def __init__(self, state_manager):
        self.state_manager = state_manager
        self.sub_state = None
        self.super_state = None

    @abstractmethod
    def initialise_state(self):
        pass

    @abstractmethod
    def enter_state(self):  # called once on state entry
        pass

    @abstractmethod
    def update_state(self):  # called every frame - contains general code
        pass

    @abstractmethod
    def check_switch_states(self):
        pass

    @abstractmethod
    def exit_state(self):  # called once on exit from state
        pass

    def reset(self):
        self.initialise_state()

    def change_sub_state(self, state):  # Can be set to None by passing in None
        if self.sub_state != state:
            if self.sub_state != None:
                self.sub_state.exit_state()
            self.sub_state = state
            if state != None:
                state.super_state = self
                state.enter_state()
        else:
            print("State already active")

    def update_states(self):
        self.check_switch_states()
        self.update_state()
        if self.sub_state:
            self.sub_state.update_states()

    def change_state(self, state, *args):
        self.state_manager.previous_state = self
        if self.super_state == None:
            if self.state_manager.current_state != state:
                print(f"changing state to {type(state)}")
                self.state_manager.current_state.exit_state()
                self.state_manager.current_state = state
                state.enter_state(*args)
            else:
                print("State already active")
        else:
            self.super_state.change_sub_state(state)
