from abc import ABC, abstractmethod


class BossBaseAttack(ABC):

    cooldown = 10
    last_shot = 0

    # conditions to be met for attack to be used
    min_distance = 0
    max_distance = 10000


    @abstractmethod
    def attack(self, state_factory):
        pass
