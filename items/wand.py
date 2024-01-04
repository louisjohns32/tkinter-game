from items.player_weapon import PlayerWeapon
from PIL import ImageTk, Image
from animation import Animation


class Wand(PlayerWeapon):
    icon_sprite = "assets/icons/wand-icon.png"
    projectile_sprite = "assets/projectiles/wand-projectile.png"

    speed = 5
    penetrate = 5

    name = "Wand"
    text = "Fires magic projectile"

    

    level_map = {
        2: {"PROJECTILES" : 2, "PRICE" : 7}, 
        3: {"DAMAGE" : 15, "PRICE" :10}, 
        4: {"PROJECTILES" : 3, "SPEED" : 10, "COOLDOWN" : 2, "PRICE" : 15}, 
        5: {"PENETRATE" : 10, "PRICE" : 20}, 
        6: {"PROJECTILES" : 4, "PRICE" : 30}, 
        7: {"DAMAGE" : 20}, 
        8: {"PROJECTILES" : 5}, 
        9: {"COOLDOWN" : 1}, 
        10: {"PROJECTILES" : 7}, 
                 }

    
