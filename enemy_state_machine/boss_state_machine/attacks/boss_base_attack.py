from abc import ABC, abstractmethod


class BossBaseAttack(ABC):

    cooldown = 10
    last_shot = 0

    @abstractmethod
    def attack(self, state_factory):
        pass
