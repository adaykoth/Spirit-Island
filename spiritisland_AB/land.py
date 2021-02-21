from .landtype import LandType
from .human import Dahan, Explorer, Town, City

class Land:
    def __init__(self, number, landType, neighbors=None):
        self.number = number
        self.landType = landType
        self.neighbors = []
        self.humans = []
        self.blight = 0

        if neighbors is not None:
            try:
                self.addNeighbors(*neighbors)
            except TypeError:
                self.addNeighbors(neighbors)

    def __repr__(self):
        humansString = ""
        if len(self.humans) > 0:
            humansString = f", {self.humans}"
        blightString = ""
        if self.blight > 0:
            blightString = f", BL={self.blight}"

        return f"Land({self.number}, {self.landType}{humansString}{blightString})"

    def isExplorable(self):
        # cannot explore oceans
        if self.landType.name == "Ocean":
            return False

        # can explore if there is at least 1 building
        for human in self.invaders:
            if human.isBuilding():
                return True

        # can build if there is at least 1 building in neighbors
        for land in self.neighbors:
            if land.landType.name == "Ocean":
                return True
            for human in land.humans:
                if human.isBuilding():
                    return True

        return False

    def isBuildable(self):
        # cannot build in oceans
        if self.landType.name == "Ocean":
            return False

        # can build if there is at least 1 invader
        for human in self.invaders:
            return True

        return False

    def isRavagable(self):
        # cannot ravage in oceans
        if self.landType.name == "Ocean":
            return False

        return True

    @property
    def dahans(self):
        return [
                human
                for human in self.humans
                    if human.name == "Dahan"
               ]

    @property
    def invaders(self):
        return [
                human
                for human in self.humans
                    if human.isInvader
        ]

    @property
    def explorers(self):
        return [
                human
                for human in self.humans
                    if human.name == "Explorer"
        ]

    @property
    def towns(self):
        return [
                human
                for human in self.humans
                    if human.name == "Town"
        ]

    @property
    def cities(self):
        return [
                human
                for human in self.humans
                    if human.name == "City"
        ]

    def addNeighbors(self, *neighbors):
        for land in neighbors:
            if land not in self.neighbors:
                self.neighbors.append(land)
            if self not in land.neighbors:
                land.addNeighbors(self)

    def removeNeighbors(self, *neighbors):
        for land in neighbors:
            if land in self.neighbors:
                self.neighbors.remove(land)
            if self in land.neighbors:
                land.neighbors.remove(self)

    def isNeighbor(self, land):
        return True if land in self.neighbors else False

    def addHumans(self, *humans):
        for human in humans:
            self.humans.append(human)

    def removeHumans(self, *humans):
        for human in humans:
            self.humans.remove(human)

    def explore(self):
        if self.isExplorable():
            print(f"Exploring {self}")
            self.addHumans(Explorer())
        else:
            print(f"Cannot explore {self}")

    def build(self):
        if self.isBuildable():
            towns = cities = 0
            for human in self.invaders:
                if human.name == "Town":
                    towns += 1
                if human.name == "City":
                    cities += 1
            if cities < towns:
                print(f"Building City in {self}")
                self.addHumans(City())
            else:
                print(f"Building Town in {self}")
                self.addHumans(Town())
        else:
            print(f"Cannot build in {self}")

    def ravage(self):
        if self.isRavagable():
            damage = 0
            for invader in self.invaders:
                damage += invader.attack

            # TODO: defend

            if damage > 0:
                print(f"Ravaging in {self} for {damage} damage.")
                self.damageLand(damage)
                self.damageDahan(damage)
                self._removeDead()

            # TODO: Dahan fight back
            retaliation = 0
            for dahan in self.dahans:
                retaliation += dahan.attack

            if retaliation > 0:
                print(f"Dahan retaliate in {self} for {retaliation} damage.")

    def damageLand(self, damage):
        if damage > 1:
            self.addBlight()

    def damageDahan(self, damage):
        # TODO: Allow for player input
        # for now: kill Dahan from oldest to youngest

        for dahan in self.dahans:
            if damage >= dahan.life:
                damage -= dahan.life
                dahan.damage(dahan.life)

    def damageInvaders(self, damage):
        # TODO: Allow for player input
        # for now: kill cities, then towns, then explorers
        for city in self.cities:
            if damage >= city.life:
                damage -= city.life
                city.damage(city.life)

        for town in self.towns:
            if damage >= town.life:
                damage -= town.life
                town.damage(town.life)

        for explorer in self.explorers:
            if damage >= explorer.life:
                damage -= explorer.life
                explorer.damage(explorer.life)

        self._removeDead()

    def _removeDead(self):
        self.humans = [
            human
            for human in self.humans
                if human.life > 0
        ]


    def addBlight(self):
        print(f"{self} is blighted.")
        self.blight += 1

        # TODO: remove presence

    def removeBlight(self, value=1):
        self.blight -= value
        if self.blight < 0:
            self.blight = 0
