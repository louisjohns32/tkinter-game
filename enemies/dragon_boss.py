from enemy import Enemy
from enemy_state_machine.dragon_boss_state_machine.dragon_state_factory import DragonStateFactory
from enemy_state_machine.boss_state_machine.attacks.charge import Charge
from animation import Animation


class DragonBoss(Enemy):
    max_health = 500
    health = max_health
    

    speed = 2

    # TODO Change how attacks are managed. Take inspiration from how i did it in soulsgame? i.e Attack objects with criteria to be met and pick a random available attack in findingAttackState]

    def __init__(self, sprite, player_ref, pos=..., collision_manager=None):
        super().__init__(sprite, player_ref, pos, collision_manager)
        self.state_factory = DragonStateFactory()
        self.current_state = self.state_factory.phase1(self)
        self.current_state.enter_state()

        self._flying_right = Animation(
            "cyberpunk-pack/red-dragon.png", (144, 128), 3, scale=2, time=64, start=3)
        self._flying_left = Animation("cyberpunk-pack/red-dragon.png",
                             (144, 128), 3, scale=2, time=64, start=9)
        self._flying_up = Animation("cyberpunk-pack/red-dragon.png",
                           (144, 128), 3, scale=2, time=64)
        self._flying_down = Animation("cyberpunk-pack/red-dragon.png",
                             (144, 128), 3, scale=2, time=64, start=6)
        self.active_anim = self._flying_right
        self.facing = "right"

    def update(self):
        super().update()

    def die(self):
        super().die()
        self.player.state_manager.BOSS.boss_dead()
