from abc import ABC, abstractmethod


class EnemyBaseState(ABC):
    level = 0  # 0 being root, its substate being 1 and so on

    def __init__(self, enemy):
        self.enemy = enemy
        self.sub_state = None
        self.super_state = None

    @abstractmethod
    def enter_state(self):  # called once on state entry
        pass

    @abstractmethod
    def update_state(self):  # called every frame - contains general code
        pass

    @abstractmethod
    def check_switch_states(self):  # called every frame - contains logic to switch states
        pass

    @abstractmethod
    def exit_state(self):  # called once on exit from state
        pass

    def change_sub_state(self, state):  # Can be set to None by passing in None
        ("Changing substate")
        if self.sub_state != None:
            self.sub_state.exit_state()
        self.sub_state = state
        if state != None:
            state.enter_state()
            state.super_state = self
            ("Super state set")

    def update_states(self):
        self.check_switch_states()
        self.update_state()
        if self.sub_state:
            self.sub_state.update_states()

    def change_state(self, state):
        (f"CHANGING STATE TO {state}")
        if self.super_state == None:
            self.enemy.current_state.exit_state()
            self.enemy.current_state = state
            state.enter_state()
        else:
            self.super_state.change_sub_state(state)
        ("STATE CHANGED")
