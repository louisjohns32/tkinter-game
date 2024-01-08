from enemies.enemy import Enemy
from enemy_state_machine.boss_state_machine.boss_state_factory import BossStateFactory
from enemy_state_machine.boss_state_machine.attacks.charge import Charge
from animation import Animation


class Boss(Enemy):
    max_health = 500
    

    radius = 100

    xp_on_pickup = 100

    # TODO Change how attacks are managed. Take inspiration from how i did it in soulsgame? i.e Attack objects with criteria to be met and pick a random available attack in findingAttackState]
    ATTACKS = [Charge()]


    def __init__(self, sprite, player_ref, pos=..., collision_manager=None):
        super().__init__(sprite, player_ref, pos, collision_manager)
        self.state_factory = BossStateFactory()
        self.current_state = self.state_factory.phase1(self)
        self.current_state.enter_state()
        self.health = self.max_health
        self.walking_right_anim = Animation(
                "../assets/../assets/cyberpunk-pack/skeleton-walk.png", (16, 22), 6, scale=8, time=64)
        self.walking_left_anim = Animation(
            "../assets/../assets/cyberpunk-pack/skeleton-walk.png", (16, 22), 6, scale=8, time=64, mirror=True)
        self.idle_right_anim = Animation(
            "../assets/../assets/cyberpunk-pack/skeleton-walk.png", (16, 22), 6, scale=8, time=64)
        self.idle_left_anim = Animation(
            "../assets/../assets/cyberpunk-pack/skeleton-walk.png", (16, 22), 6, scale=8, time=64, mirror=True)

    def update(self):
        super().update()

    def die(self):
        super().die()
        self.player.state_manager.BOSS.boss_dead()
