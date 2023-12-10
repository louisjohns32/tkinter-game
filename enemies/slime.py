from enemy import Enemy
from animation import Animation


class Slime(Enemy):
    walking_right_anim = Animation(
        "cyberpunk-pack/slime.png", (8, 6), 2, scale=8, time=100)
    walking_left_anim = Animation(
        "cyberpunk-pack/slime.png", (8, 6), 2, scale=8, time=100, mirror=True)
    idle_left_anim = Animation(
        "cyberpunk-pack/slime.png", (8, 6), 2, scale=8, time=100)
    idle_right_anim = Animation(
        "cyberpunk-pack/slime.png", (8, 6), 2, scale=8, time=100, mirror=True)
    speed = 2
    max_health = 10
    health = max_health

    type = "Slime"
