from enemy_dumb import EnemyDumb
from animation import Animation


class Rat(EnemyDumb):
    move_l_anim_args = ["cyberpunk-pack/rat-walk.png", (32, 20), 3]
    move_l_anim_kwargs = {"scale":2, "time":60, "mirror":True}
    move_r_anim_args = move_l_anim_args
    move_r_anim_kwargs =  {"scale":2, "time":60}

    SPEED = 5
        