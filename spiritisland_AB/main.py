from .island import Island
from .land import Land
from .landtype import LandType
from .human import Human, Dahan, Explorer, Town, City
from .deck import InvaderDeck, InvaderCard

OCEAN = LandType("Ocean")
SANDS = LandType("Sands")
WETLANDS = LandType("Wetlands")
JUNGLE = LandType("Jungle")
MOUNTAINS = LandType("Mountains")

def loadMap(name):
    if name == "A":
        t0 = Land(0, OCEAN)
        t1 = Land(1, MOUNTAINS, neighbors = t0)
        t2 = Land(2, WETLANDS, neighbors = [t0, t1])
        t3 = Land(3, JUNGLE, neighbors = [t0, t2])
        t4 = Land(4, SANDS, neighbors = [t1, t2, t3])
        t5 = Land(5, WETLANDS, neighbors = [t1, t4])
        t6 = Land(6, MOUNTAINS, neighbors = [t1, t4, t5])
        t7 = Land(7, SANDS, neighbors = t5)
        t8 = Land(8, JUNGLE, neighbors = [t5, t6, t7])
        t2.addHumans(City(), Dahan())
        t3.addHumans(Dahan(), Dahan())
        t4.addBlight()
        t5
        t6.addHumans(Dahan())
        t7.addHumans(Dahan(), Dahan())
        t8.addHumans(Town())

        return Island([t0, t1, t2, t3, t4, t5, t6, t7, t8])
    else:
        raise NotImplementedError(f"Map {name} not available.")

def loadInvaderDeck():
    invaderDeckStage1 = InvaderDeck([
        InvaderCard(JUNGLE),
        InvaderCard(WETLANDS),
        InvaderCard(SANDS)
    ])
    invaderDeckStage2 = InvaderDeck([
        InvaderCard(SANDS, escalation = True),
        InvaderCard(MOUNTAINS, escalation = True),
        InvaderCard(JUNGLE, escalation = True),
        InvaderCard(WETLANDS, escalation = True)
    ])
    invaderDeckStage3 = InvaderDeck([
        InvaderCard(SANDS, MOUNTAINS),
        InvaderCard(SANDS, WETLANDS),
        InvaderCard(JUNGLE, WETLANDS),
        InvaderCard(JUNGLE, SANDS),
        InvaderCard(MOUNTAINS, JUNGLE)
    ])

    invaderDeck = invaderDeckStage1
    invaderDeck.cards.extend(invaderDeckStage2.cards)
    invaderDeck.cards.extend(invaderDeckStage3.cards)

    return invaderDeck
