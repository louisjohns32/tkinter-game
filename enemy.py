from game_object import GameObject
from enemy_state_machine.enemy_state_factory import EnemyStateFactory
from PIL import ImageTk


class Enemy(GameObject):
    max_health = 10
    health = max_health
    player = None
    current_state = None
    state_factory = EnemyStateFactory()

    # stats
    speed = 1
    damage = 1
    xp_on_pickup = 1

    # animations all enemies should have
    walking_left_anim = None
    walking_right_anim = None
    idle_left_anim = None
    idle_right_anim = None

    facing = "right"

    tag = "enemy"
    type = "Enemy"

    def __init__(self, sprite, player_ref, pos=(0, 0), collision_manager=None):
        super().__init__(sprite, pos=pos, collision_manager=collision_manager)
        self.player = player_ref
        self.current_state = self.state_factory.chasing(self)
        self.current_state.enter_state()
        self.health = self.max_health
        self.active_anim = self.walking_right_anim

    def die(self):
        self.health = 0
        self.current_state.change_state(self.state_factory.dead(self))

    def take_damage(self, dmg):
        self.health -= dmg
        if self.health <= 0:
            self.die()

    def recoverHealth(self, health):
        self.health = min(self.max_health, self.health+health)

    def update(self):
        super().update()

        # update states
        state = self.current_state
        while state:
            state.update_states()
            state = state.sub_state

       # animation stuff
        self.active_anim.update()
        self.sprite = ImageTk.PhotoImage(self.active_anim.get_sprite())

    def save(self): # stores and formats enemy info into save_dict and returns it to be saved
        save_dict = super().save()
        save_dict["health"] = self.health

        return save_dict

    def load(self, info): # unloads save info 
        super().load(info)
        self.health = info["health"]
        if self.health <= 0:
            self.current_state.change_state(self.state_factory.dead(self))
