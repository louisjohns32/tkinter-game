from enemy_dumb import Enemy
from animation import Animation


class Slime(Enemy):
    def __init__(self, sprite, player_ref, pos=(0,0), collision_manager=None):
        super().__init__(sprite, player_ref, pos, collision_manager)

        if self.walking_right_anim == None:
            self.walking_right_anim = Animation(
            "cyberpunk-pack/slime.png", (8, 6), 2, scale=8, time=100)
            self.walking_left_anim = Animation(
            "cyberpunk-pack/slime.png", (8, 6), 2, scale=8, time=100, mirror=True)
            self.idle_left_anim = Animation(
            "cyberpunk-pack/slime.png", (8, 6), 2, scale=8, time=100)
            self.idle_right_anim = Animation(
            "cyberpunk-pack/slime.png", (8, 6), 2, scale=8, time=100, mirror=True)
            self.speed = 2
            self.max_health = 10
            self.health = self.max_health

    type = "Slime"
