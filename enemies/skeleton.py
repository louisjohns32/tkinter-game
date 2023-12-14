from enemy import Enemy
from animation import Animation


class Skeleton(Enemy):
    def __init__(self, sprite, player_ref, pos=(0,0), collision_manager=None):
        super().__init__(sprite, player_ref, pos, collision_manager)

        if self.walking_right_anim == None: 
            self.walking_right_anim = Animation(
            "cyberpunk-pack/skeleton-walk.png", (16, 22), 6, scale=4, time=64)
            self.walking_left_anim = Animation(
            "cyberpunk-pack/skeleton-walk.png", (16, 22), 6, scale=4, time=64, mirror=True)
            self.idle_right_anim = Animation(
            "cyberpunk-pack/skeleton-walk.png", (16, 22), 6, scale=4, time=64)
            self.idle_left_anim = Animation(
            "cyberpunk-pack/skeleton-walk.png", (16, 22), 6, scale=4, time=64, mirror=True)

        self.speed = 1.5
        self.damage = 5
        self.max_health = 20
        self.health = self.max_health

    type = "Skeleton"
