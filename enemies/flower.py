from enemy import Enemy
from animation import Animation


class Flower(Enemy):
    

    type = "Flower"

    def __init__(self, sprite, player_ref, pos=(0,0), collision_manager=None):
        super().__init__(sprite, player_ref, pos, collision_manager)
        self.walking_right_anim = Animation(
        "cyberpunk-pack/man_eater_flower.png", (128, 128), 6, scale=1, time=60, start=18)
        self.walking_left_anim = Animation(
        "cyberpunk-pack/man_eater_flower.png", (128, 128), 6, scale=1, time=60, start=18, mirror=True)
        self.idle_right_anim = Animation(
        "cyberpunk-pack/man_eater_flower.png", (128, 128), 6, scale=1, time=60, start=18)
        self.idle_left_anim = Animation("cyberpunk-pack/man_eater_flower.png",
                               (128, 128), 6, scale=1, time=60, start=18, mirror=True)
        self.speed = 2

        self.max_health = 20
        self.health = self.max_health
