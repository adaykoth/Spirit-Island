from Classes.Invader import Invader
import random


global Lands


class Land:
    def __init__(self, landid, landtype, blight, connections, invaders, theisland):
        self.landid = landid
        self.landtype = landtype
        self.blight = blight
        self.connections = connections
        self.invaders = invaders
        self.theisland = theisland

    def is_explorable(self):
        # if is ocean
        if self.landtype == "Ocean":
            return False
        # if next to ocean
        elif 0 in self.connections:
            return True
        # if contains buildings
        elif self.landid in [
                x.position for x in list(filter(lambda x: x.invtype == "City" or x.invtype == "Village", self.invaders))]:
            return True
        # if surrounding lands contain buildings
        elif list(set(self.connections) & set([
                x.position for x in list(filter(lambda x: x.invtype == "City" or x.invtype == "Village", self.invaders))])):
            return True
        else:
            return False

    def is_invaded(self):
        # if is ocean
        if self.landtype == "Ocean":
            return False
        # if there is an invader present
        elif self.landid in [x.position for x in self.invaders]:
            return True

    def is_coastal(self):
        if 0 in self.connections:
            return True
        else:
            return False

    def add_explorer(self, number=1):
        for i in range(0, number):
            self.invaders.append(Invader("Explorer", 1, 1, self.landid))
            print("Added Explorer at " + str(self.landid))

    def add_building(self, number=1):
        for i in range(0, number):
            land_villages = list(filter(lambda x: x.invtype == "Village" and x.position == self.landid, self.invaders))
            print("Amount of villages in " + str(self.landid) + " " + str(land_villages.__len__()))
            land_cities = list(filter(lambda x: x.invtype == "Cities" and x.position == self.landid, self.invaders))
            print("Amount of cities in " + str(self.landid) + " " + str(land_cities.__len__()))
            if land_cities.__len__() < land_villages.__len__():
                self.invaders.append(Invader("City", 3, 3, self.landid))
                print("Added City at " + str(self.landid))
            else:
                self.invaders.append(Invader("Village", 2, 2, self.landid))
                print("Added Village at " + str(self.landid))

    def ravage(self):
        land_invader_damage = sum([x.damage for x in list(filter(lambda x: x.position == self.landid, self.invaders))])
        print(str(land_invader_damage) + " Damage to land " + str(self.landid))
        if land_invader_damage > 1:
            print("Damage to land is greater than 1. Adding blight")
            self.add_blight()

    def add_blight(self):
        if self.blight == 0:
            self.blight += 1
            self.theisland.remove_blight()
        else:
            self.blight += 1
            self.theisland.remove_blight()
            # YOU SHOULD CHOOSE A LAND !!!
            if self.theisland.blight > 0:
                print("Blight cascades to an adjacent land")
                cascade_land = random.choice(Lands[4].connections)
                next((x for x in Lands if x.landid == cascade_land)).add_blight()

    def get_lands_in_range(self, lrange=1):
        landids = set(self.connections + [self.landid])
        if lrange == 0:
            return {self.landid}
        elif lrange > 1:
            while lrange > 1:
                landids2 = []
                for x in landids:
                    landids2 += Lands[x].connections
                landids.update(landids2)
                lrange -= 1
        return landids
