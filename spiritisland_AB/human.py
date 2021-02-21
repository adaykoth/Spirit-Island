class Human:
    def __init__(self, name, maxLife, maxAttack, isInvader, isBuilding):
        self.name = name
        self.life = self.maxLife = maxLife
        self.attack = self.maxAttack = maxAttack
        self.isInvader = isInvader
        self.isBuilding = isBuilding

    @property
    def isBuilding(self):
        return _isBuilding
    @isBuilding.setter
    def isBuilding(self, value):
        self._isBuilding = value

    def reset(self):
        self.attack = self.maxAttack
        self.heal()

    def heal(self):
        self.life = self.maxLife

    def damage(self, attack):
        self.life -= attack
        if self.life <= 0:
            self.kill()

    def kill(self):
        self.life = 0
        print(f"{self.name} dies.")

    def __repr__(self):
        lifeString = ""
        if self.life != self.maxLife:
            lifeString = f", {self.life}/{self.maxLife}"
        attackString = ""
        if self.attack != self.maxAttack:
            attackString = f", ATK={self.attack}"

        if lifeString == attackString == "":
            return f"{self.name}"
        return f"{self.name}({lifeString}{attackString})"

class Dahan(Human):
    def __init__(self):
        super().__init__(name = "Dahan", maxLife = 2, maxAttack = 2,
                         isInvader = False, isBuilding = False)

class Explorer(Human):
    def __init__(self):
        super().__init__(name = "Explorer", maxLife = 1, maxAttack = 1,
                         isInvader = True, isBuilding = False)

class Town(Human):
    def __init__(self):
        super().__init__(name = "Town", maxLife = 2, maxAttack = 2,
                         isInvader = True, isBuilding = True)

class City(Human):
    def __init__(self):
        super().__init__(name = "City", maxLife = 3, maxAttack = 3,
                         isInvader = True, isBuilding = True)
