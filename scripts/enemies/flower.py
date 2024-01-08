from enemies.enemy_dumb import EnemyDumb
from animation import Animation


class Flower(EnemyDumb):
    

    move_l_anim_args = ["../assets/cyberpunk-pack/man_eater_flower.png", (128, 128), 6]
    move_r_anim_args = move_l_anim_args
    move_r_anim_kwargs = {"scale":1, "time":60,"start":18}
    move_l_anim_kwargs = {"scale":1, "time":60,"start":18, "mirror":True}

