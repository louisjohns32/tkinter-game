from enemy_state_machine.enemy_base_state import EnemyBaseState
import random as rand
from camera import Camera
from Window import Window


class DragonPhase2State(EnemyBaseState):
    ATTACKS = []

    def enter_state(self):
        self.enemy.ATTACKS = self.ATTACKS

        self.order = rand.randint(0,1) # first is middle, then bottom if 0 or 1 if top

        edges = Camera.instance.get_edges()
        self.change_sub_state(
            self.enemy.state_factory.moveTo(self.enemy,(edges[0][0]+10, self.enemy.player.y_pos),speed_multiplier=2, 
                                            next_state=self.enemy.state_factory.devestate(self.enemy, False)))
                                            
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
        pass
