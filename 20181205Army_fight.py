# Army fight with another
import logging
logging.basicConfig(level=logging.INFO)


class Warrior(object):
    def __init__(self, health=50, attack=5):
        self.health = health
        self.attack = attack
        self.is_alive = True

class Knight(Warrior):
    def __init__(self):
        super().__init__()
        self.attack = 7
        self.is_alive = True

class Army(object):
    def __init__(self):
        pass
    def add_units(self, _soldier='Warrior', _count=0):
        self._soldier = _soldier
        self._count = _count
        return self._soldier,self._count

def fight():
    pass

my_army = Army()
my_army.add_units('Warrior', 3)
logging.info(my_army.add_units('Warrior', 3))
em_army = Army()
em_army.add_units('Knight', 4)
logging.info(my_army.add_units('Knight', 4))

