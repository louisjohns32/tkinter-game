from game_state_machine.game_base_state import GameBaseState
from Window import Window


class BossState(GameBaseState):
    def initialise_state(self):
        pass

    def enter_state(self):
        # lock camera
        self.super_state.camera.lock_pos(True)
        self.super_state.camera.shake()
        # create boss healthbar
        pass

    def exit_state(self):
        # unlock camera pos
        self.super_state.camera.lock_pos(False)
        # destroy boss healthbar
        pass

    def update_state(self):
        # update boss healthbar
        self.state_manager.main_canvas.create_rectangle(
            Window.WIDTH/2-400, 0, Window.WIDTH/2 + 400, 100, fill="black")
        self.state_manager.main_canvas.create_rectangle(
            Window.WIDTH/2-400, 0, (Window.WIDTH/2 - 400 + 800*(self.boss.health/self.boss.max_health)), 100, fill="red")

    def check_switch_states(self):
        # check if boss is dead
        pass

    def boss_dead(self):
        self.super_state.change_sub_state(None)
       # self.state_manager.PLAYING.enemy_spawner.nextWave()

    def set_boss_ref(self, boss):  # set boss reference
        self.boss = boss
