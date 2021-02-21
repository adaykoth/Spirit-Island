class Spirit:
    def __init__(self, name, energy_per_turn=0, card_plays_per_turn=0, power_cards_in_hand=None):
        self.name = name
        self.energy = 0
        self.energy_per_turn = energy_per_turn
        self.card_plays_per_turn = card_plays_per_turn
        self.presences = {"On Track": 13, "Lost": 0, "In Play": []}
        self.elements = {"Sun": 0, "Moon": 0, "Fire": 0, "Air": 0, "Water": 0, "Earth": 0, "Plant": 0, "Animal": 0}
        self.power_cards_in_hand = power_cards_in_hand
        self.power_cards_in_play = None
        self.power_cards_discarded = None

    def setup(self, lands):
        if self.name == "Shadows Flicker Like Flame":
            self.presences["On Track"] -= 3
            starting_position = [
                list(filter(lambda x: x.landtype == "Jungle", lands))[-1].landid,
                list(filter(lambda x: x.landtype == "Jungle", lands))[-1].landid,
                5
            ]
            self.presences["In Play"] = starting_position

    def growth(self):
        if self.name == "Shadows Flicker Like Flame":
            print("Growth (Pick One)")
            selection = int(input("Reclaim Cards, Gain Power Card (1)  |  Gain Power Card, Add a Presence in Range 1 "
                                  "(2)  |  Add a Presence in Range 3, Gain 3 Energy (3)"))
            if selection == 1:
                print("Picked (1)")
                self.reclaim_power_cards()
                self.gain_power_card()
            elif selection == 2:
                print("Picked (2)")
                self.gain_power_card()
                self.add_presence(1)
            elif selection == 3:
                print("Picked (3)")
                self.add_presence(3)
                self.energy += 3

    def reclaim_power_cards(self):
        pass

    def gain_power_card(self):
        pass

    def add_presence(self, growth_range, lands):
        if self.presences["On Track"] > 0:
            self.presences["On Track"] -= 1
        elif self.presences["Lost"] > 0:
            pass
        else:
            pass
        landids = set()
        for x in self.presences["In Play"]:
            landids.update(lands,[x].get_lands_in_range(growth_range))
        selection = input(str(landids))
        print(self.name + " adds presence to land " + selection)
        self.presences["In Play"].append(int(selection))

