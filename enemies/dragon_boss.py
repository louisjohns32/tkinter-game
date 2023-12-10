from enemy import Enemy
from enemy_state_machine.dragon_boss_state_machine.dragon_state_factory import DragonStateFactory
from enemy_state_machine.boss_state_machine.attacks.charge import Charge
from animation import Animation


class DragonBoss(Enemy):
    max_health = 500
    health = max_health
    _flying_right = Animation(
        "cyberpunk-pack/red-dragon.png", (144, 128), 12, scale=2, time=64, start=3, end=5)
    _flying_left = Animation("cyberpunk-pack/red-dragon.png",
                             (144, 128), 12, scale=2, time=64, start=9, end=11)
    _flying_up = Animation("cyberpunk-pack/red-dragon.png",
                           (144, 128), 12, scale=2, time=64, start=0, end=2)
    _flying_down = Animation("cyberpunk-pack/red-dragon.png",
                             (144, 128), 12, scale=2, time=64, start=6, end=8)
    active_anim = _flying_right
    facing = "right"

    speed = 2

    # TODO Change how attacks are managed. Take inspiration from how i did it in soulsgame? i.e Attack objects with criteria to be met and pick a random available attack in findingAttackState]

    def __init__(self, sprite, player_ref, pos=..., collision_manager=None):
        super().__init__(sprite, player_ref, pos, collision_manager)
        self.state_factory = DragonStateFactory()
        self.current_state = self.state_factory.phase1(self)
        self.current_state.enter_state()

    def update(self):
        super().update()

    def die(self):
        super().die()
        self.player.state_manager.BOSS.boss_dead()
