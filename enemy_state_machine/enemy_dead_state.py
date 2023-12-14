from enemy_state_machine.enemy_base_state import EnemyBaseState
from animation import Animation
from time import time


class EnemyDeadState(EnemyBaseState):

    def enter_state(self):
        print("ENTERED DEAD STATE")
        # set sprite to xp pickup
        self.enemy.active_anim = Animation(
            "cyberpunk-pack/xp-pickup.png", (64, 64), 1, scale=0.5)
        # remove from collidable objects
        self.enemy.collision_manager.remove_object(self.enemy)
        self.enemy.collidable = False
        self.start_time = time()
        self.del_time = 5

        self.enemy.player.state_manager.PLAYING.addScore(
            self.enemy.xp_on_pickup)

    def update_state(self):
        pass

    def exit_state(self):
        pass

    def check_switch_states(self):
        # check if player has collided to pick up obj
        x = self.enemy.player.x_pos - self.enemy.x_pos
        y = self.enemy.player.y_pos - self.enemy.y_pos

        if abs(x) < 80 and abs(y) < 80:
            self.enemy.player.increaseXP(self.enemy.xp_on_pickup)
            self.enemy.player.obj_manager.delete_object(self.enemy)
            self.enemy.deactivate() # TODO MOVE THIS!!!!!!

        elif time() > self.start_time + self.del_time:
            self.enemy.player.obj_manager.delete_object(self.enemy)
            self.enemy.deactivate() # TODO MOVE THIS!!!
