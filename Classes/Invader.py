class Invader:
    def __init__(self, invtype, damage, health, position):
        self.invtype = invtype
        self.damage = damage
        self.health = health
        self.position = position

    def ravage(self):
        print(self.invtype + " ravages at position " + str(self.position))
