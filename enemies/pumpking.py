from enemy_dumb import EnemyDumb
from animation import Animation


class Pumpking(EnemyDumb):
    move_l_anim_args = ["cyberpunk-pack/pumpking.png", (64, 64), 3]
    move_r_anim_args = move_l_anim_args
    move_l_anim_kwargs = {"scale":1.5, "time":60,"start":6}
    move_r_anim_kwargs = {"scale":1.5, "time":60,"start":6, "mirror":True}

    MAX_HEALTH = 20
    SPEED = 1.5

