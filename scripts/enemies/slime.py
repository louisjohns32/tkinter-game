from enemies.enemy_dumb import EnemyDumb


class Slime(EnemyDumb):
    move_l_anim_args = ["../assets/../assets/cyberpunk-pack/slime.png", (8, 6), 2]
    move_l_anim_kwargs = {"scale":8, "time":100, "mirror":True}
    move_r_anim_args = ["../assets/../assets/cyberpunk-pack/slime.png", (8, 6), 2]
    move_r_anim_kwargs = {"scale":8, "time":100}

    SPEED = 2

   