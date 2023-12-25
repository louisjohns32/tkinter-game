from enemy_dumb import EnemyDumb
from animation import Animation


class Skeleton(EnemyDumb):
    move_l_anim_args = ["cyberpunk-pack/skeleton-walk.png", (16, 22), 6]
    move_l_anim_kwargs = {"scale":4, "time":64, "mirror":True}
    move_r_anim_args = ["cyberpunk-pack/skeleton-walk.png", (16, 22), 6]
    move_r_anim_kwargs = {"scale":4, "time":64}
    
    SPEED = 2.5
    MAX_HEALTH = 20



  