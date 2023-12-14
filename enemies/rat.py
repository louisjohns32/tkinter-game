from enemy import Enemy
from animation import Animation


class Rat(Enemy):
    def __init__(self, sprite, player_ref, pos=(0,0), collision_manager=None):
        super().__init__(sprite, player_ref, pos, collision_manager)
        self.walking_right_anim = Animation(
        "cyberpunk-pack/rat-walk.png", (32, 20), 3, scale=2, time=60)
        self.walking_left_anim = Animation(
        "cyberpunk-pack/rat-walk.png", (32, 20), 3, scale=2, time=60, mirror=True)
        self.idle_right_anim = Animation(
        "cyberpunk-pack/rat-walk.png", (32, 20), 3, scale=2, time=60)
        self.idle_left_anim = Animation(
        "cyberpunk-pack/rat-walk.png", (32, 20), 3, scale=2, time=60, mirror=True)
        self.speed = 8
        self.damage = 1

        self.max_health = 10
        self.health = self.max_health

    type = "Rat"
