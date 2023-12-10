from enemy_state_machine.enemy_base_state import EnemyBaseState


class DragonPhase2State(EnemyBaseState):
    ATTACKS = []

    def enter_state(self):
        ("ENTERED PHASE 1 STATE")
        self.enemy.ATTACKS = self.ATTACKS
        self.change_sub_state(
            self.enemy.state_factory.moveTo(self.enemy, (200, 200)))
        # SET SUBSTATE TO GOTO, SETTING THE POSITION OFF SCREEN AT EITHER THE TOP OR BOTTOM THIRD
        # CHANGE STATE TO DEVESTATE WITHIN GOTO, AND SPREAD FIRE ACCROSS SECTION
        # REPEAT THIS FOR EACH THIRD

        # WHEN THE MAGMA DIES, BOSS FLIES DOWN AND IS STUNNED FOR 5 SECONDS WHILST SPAWNING ANOTHER MAGMA, THIS CANCELS ANY FUTURE DEVESTATES IN THAT PHASE
    def update_state(self):
     #   if self.sub_state == None:
        #  self.change_sub_state(self)
        pass

    def exit_state(self):
        pass

    def check_switch_states(self):
        # check for phase2 switch
        if self.enemy.health < 400:
            self.change_state(self.enemy.state_factory.phase2(self.enemy))
