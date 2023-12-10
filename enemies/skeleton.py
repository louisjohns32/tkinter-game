from enemy import Enemy
from animation import Animation


class Skeleton(Enemy):
    walking_right_anim = Animation(
        "cyberpunk-pack/skeleton-walk.png", (16, 22), 6, scale=4, time=64)
    walking_left_anim = Animation(
        "cyberpunk-pack/skeleton-walk.png", (16, 22), 6, scale=4, time=64, mirror=True)
    idle_right_anim = Animation(
        "cyberpunk-pack/skeleton-walk.png", (16, 22), 6, scale=4, time=64)
    idle_left_anim = Animation(
        "cyberpunk-pack/skeleton-walk.png", (16, 22), 6, scale=4, time=64, mirror=True)

    speed = 1.5
    damage = 5
    max_health = 20
    health = max_health

    type = "Skeleton"
