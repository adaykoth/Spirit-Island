# Import(ant) modules

import random
# import os
from Classes.Dahan import Dahan
from Classes.Invader import Invader
from Classes.InvaderCard import InvaderCard
from Classes.Island import Island
from Classes.Land import Land
from Classes.PowerCard import PowerCard
from Classes.Spirit import Spirit
# Classes and so on
# Required for the rest

TheIsland = Island()

####################
# Setup begins here

global Lands
global Invaders
global Dahans
global InvaderCards
global FearCards
global BlightCard
global MajorPowerCards
global MinorPowerCards


def setup_island():

    global Lands
    Lands = [
        Land(0, "Ocean", 0, [1, 2, 3]),
        Land(1, "Mountain", 0, [0, 2, 4, 5, 6]),
        Land(2, "Wetland", 0, [0, 1, 3, 4]),
        Land(3, "Jungle", 0, [0, 2, 4]),
        Land(4, "Sands", 1, [1, 2, 3, 5]),
        Land(5, "Wetland", 0, [1, 4, 6, 7, 8]),
        Land(6, "Mountain", 0, [1, 5, 8]),
        Land(7, "Sands", 0, [5, 8]),
        Land(8, "Jungle", 0, [5, 6, 7])
    ]

    global Invaders
    Invaders = [
        Invader("City", 3, 3, 2),
        Invader("Village", 2, 2, 8)
    ]

    global Dahans
    Dahans = [
        Dahan(2, 2),
        Dahan(2, 3),
        Dahan(2, 3),
        Dahan(2, 6),
        Dahan(2, 7),
        Dahan(2, 7)
    ]


def setup_invader_cards(stage1cards=3, stage2cards=4, stage3cards=5):
    global InvaderCards
    invader_cards_s1 = [
        InvaderCard(0, 1, "Mountain"),
        InvaderCard(1, 1, "Wetland"),
        InvaderCard(2, 1, "Jungle"),
        InvaderCard(3, 1, "Sands"),
    ]
    invader_cards_s2 = [
        InvaderCard(4, 2, "Mountain"),
        InvaderCard(5, 2, "Wetland"),
        InvaderCard(6, 2, "Jungle"),
        InvaderCard(7, 2, "Sands"),
        InvaderCard(8, 2, "Coastal"),
    ]
    invader_cards_s3 = [
        InvaderCard(9, 3, "Mountain", "Wetland"),
        InvaderCard(10, 3, "Mountain", "Jungle"),
        InvaderCard(11, 3, "Mountain", "Sands"),
        InvaderCard(12, 3, "Jungle", "Wetland"),
        InvaderCard(13, 3, "Jungle", "Sands"),
        InvaderCard(14, 3, "Sands", "Wetland"),
    ]

    while invader_cards_s1.__len__() > stage1cards:
        invader_cards_s1.pop(random.randint(0, invader_cards_s1.__len__() - 1))
    while invader_cards_s2.__len__() > stage2cards:
        invader_cards_s2.pop(random.randint(0, invader_cards_s2.__len__() - 1))
    while invader_cards_s3.__len__() > stage3cards:
        invader_cards_s3.pop(random.randint(0, invader_cards_s3.__len__() - 1))

    random.shuffle(invader_cards_s1)
    random.shuffle(invader_cards_s2)
    random.shuffle(invader_cards_s3)

    InvaderCards = invader_cards_s1 + invader_cards_s2 + invader_cards_s3

    for card in InvaderCards:
        print(card.invcardid, card.stage, card.land1, card.land2)


def setup_power_cards():
    global MinorPowerCards
    global MajorPowerCards

    MajorPowerCards = [
        PowerCard(0, "Concealing Shadows", 0, "Fast", ["Moon", "Air"], 0, "Land"),
        PowerCard(1, "Crops Wither and Fade", 1, "Slow", ["Moon", "Fire", "Plant"], 0, "Land"),
        PowerCard(2, "Favors Called Due", 1, "Slow", ["Moon", "Air"], 1, "Land"),
        PowerCard(3, "Mantle of Dread", 1, "Slow", ["Moon", "Fire", "Air"], 0, "Spirit")
    ]


setup_island()
setup_invader_cards()
Player1 = Spirit("Shadows Flicker Like Flame")
Player1.setup(Lands)
###################
# Game starts


def explore():

    # End game if no explorer cards can be drawn
    if TheIsland.turn > InvaderCards.__len__()-1:
        print("\nInvader cards exhausted. You lost the island to the invaders!\n  --  Game Over  --")
    else:
        print("\nExplore in: " + InvaderCards[TheIsland.turn].land1)
        for land in Lands:
            # if land matches current explorer card
            if land.landtype == InvaderCards[TheIsland.turn].land1 and land.is_explorable(Invaders):
                print("Land " + str(land.landid))
                land.add_explorer()
            # if land is coastal
            elif InvaderCards[TheIsland.turn].land1 == "Coastal" and land.is_coastal():
                print("Land " + str(land.landid))
                land.add_explorer()

        # if there is a second land on the card (stage 3)
        if InvaderCards[TheIsland.turn].land2:
            print("Explore in: " + InvaderCards[TheIsland.turn].land2)
            for land in Lands:
                # if land matches current explorer card
                if land.landtype == InvaderCards[TheIsland.turn].land2 and land.is_explorable(Invaders):
                    print("Land " + str(land.landid))
                    land.add_explorer()


def build():
    # skip turn 0
    if TheIsland.turn > 0:
        print("\nBuild in: " + InvaderCards[TheIsland.turn - 1].land1)
        for land in Lands:
            # if land matches current build card
            if land.landtype == InvaderCards[TheIsland.turn - 1].land1 and land.is_invaded():
                print("Land " + str(land.landid))
                land.add_building()
            # if land is coastal
            elif InvaderCards[TheIsland.turn - 1].land1 == "Coastal" and land.is_coastal() and land.is_invaded():
                print("Land " + str(land.landid))
                land.add_building()

    # if there is a second land on the card (stage 3)
        if InvaderCards[TheIsland.turn - 1].land2:
            print("Build in: " + InvaderCards[TheIsland.turn - 1].land2)
            for land in Lands:
                # if land matches current build card
                if land.landtype == InvaderCards[TheIsland.turn - 1].land2 and land.is_invaded():
                    print("Land " + str(land.landid))
                    land.add_building()


def ravage():
    # skip turn 0 and 1
    if TheIsland.turn > 1:
        print("\nRavage in: " + InvaderCards[TheIsland.turn - 2].land1)
        for land in Lands:
            # if land matches current ravage card
            if land.landtype == InvaderCards[TheIsland.turn - 2].land1 and land.is_invaded():
                print("Land " + str(land.landid))
                land.ravage()
            # if land is coastal
            elif InvaderCards[TheIsland.turn - 2].land1 == "Coastal" and land.is_coastal() and land.is_invaded():
                print("Land " + str(land.landid))
                land.ravage()

    # if there is a second land on the card (stage 3)
        if InvaderCards[TheIsland.turn - 2].land2:
            print("Ravage in: " + InvaderCards[TheIsland.turn - 2].land2)
            for land in Lands:
                # if land matches current ravage card
                if land.landtype == InvaderCards[TheIsland.turn - 2].land2 and land.is_invaded():
                    print("Land " + str(land.landid))
                    land.ravage()


while TheIsland.turn < 13:
    ravage()
    if TheIsland.blight <= 0 and not TheIsland.healthy:
        break
    build()
    explore()
    TheIsland.turn += 1

for y in Invaders:
    # print(y.invtype + " in " + str(y.position))
    pass
