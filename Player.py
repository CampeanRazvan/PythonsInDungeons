class Player:
    def __init__(self, name, mana, health, damage):
        self.name = name
        self.mana = mana
        self.health = health
        self.damage = damage


    def atack(self):
        pass

class Warior(Player):

    def __init__(self, name, mana, health, damage):
        super.__init__(name, mana(0), health(10), damage(10))

class Wizard(Player):

    def __init__(self, name, mana, health, damage):
        super.__init__(name, mana(10), health(10), damage(10))

