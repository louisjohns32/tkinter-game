from enemy_state_machine.enemy_base_state import EnemyBaseState


class EnemyAttackingState(EnemyBaseState):
    def enter_state(self):
        ("ENTERED ATTACKING STATE")

    def exit_state(self):
        pass

    def check_switch_states(self):
        x = self.enemy.player.x_pos - self.enemy.x_pos
        y = self.enemy.player.y_pos - self.enemy.y_pos
        if abs(x) > 40 or abs(y) > 80:
            self.change_state(self.enemy.state_factory.chasing(
                self.enemy))  # TODO Super messy, maybe change???

    def update_state(self):
        self.enemy.player.take_damage(self.enemy.damage)

        if self.enemy.facing == "left":  # TODO Checking this in an if statement every tick feels messy
            self.enemy.active_anim = self.enemy.idle_left_anim
        else:
            self.enemy.active_anim = self.enemy.idle_right_anim
