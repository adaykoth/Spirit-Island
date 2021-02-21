class PowerCard:
    def __init__(self, powcardid, name, energy, speed, elements, target_range, target_type):
        self.powcardid = powcardid
        self.name = name
        self.energy = energy
        self.speed = speed  # Fast, Slow
        self.elements = elements  # Sun, Moon, Fire, Air, Water, Earth, Plant, Animal
        self.target_range = target_range
        self.target_type = target_type

    def concealing_shadows(self):
        if self.name == "Concealing Shadows":
            pass
