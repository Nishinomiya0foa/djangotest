# 创建战士类（50血，5攻） 骑士类（继承战士类 7攻）
# 创建fight  A攻击B B掉血 然后反之  重复
# 若A health>0  return True  反之 False
class warrior(object):
    def __init__(self, health=50, attack=5):
        self.health = health
        self.attack = attack
        self.is_alive = True

class knight(warrior):
    def __init__(self):
        super().__init__()
        self.attack = 7
        self.is_alive = True

def fight(a, b):
    while True:
        b.health = b.health - a.attack
        if b.health <= 0:
            b.is_alive = False
            return True
        a.health = a.health - b.attack
        if a.health <= 0:
            a.is_alive = False
            return False

if __name__ == '__main__':
    chuck = warrior()
    bruce = warrior()
    carl = knight()
    dave = warrior()
    print(fight(chuck, bruce))
    print(fight(dave, carl))
    print(chuck.is_alive)
    print(bruce.is_alive)
    print(carl.is_alive)
    print(dave.is_alive)