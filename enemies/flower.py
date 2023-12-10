from enemy import Enemy
from animation import Animation


class Flower(Enemy):
    walking_right_anim = Animation(
        "cyberpunk-pack/man_eater_flower.png", (128, 128), 6, scale=1, time=60, start=18)
    walking_left_anim = Animation(
        "cyberpunk-pack/man_eater_flower.png", (128, 128), 6, scale=1, time=60, start=18, mirror=True)
    idle_right_anim = Animation(
        "cyberpunk-pack/man_eater_flower.png", (128, 128), 6, scale=1, time=60, start=18)
    idle_left_anim = Animation("cyberpunk-pack/man_eater_flower.png",
                               (128, 128), 6, scale=1, time=60, start=18, mirror=True)
    speed = 2

    max_health = 20
    health = max_health

    type = "Flower"
