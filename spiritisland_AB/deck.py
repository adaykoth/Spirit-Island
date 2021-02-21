import random

class Deck:
    def __init__(self, cards):
        self.cards = cards
        self.discards = []
        self.shuffle()
        self.emptyFunc = None

    def __repr__(self):
        return f"Deck{self.cards}"

    def __len__(self):
        return len(self.cards)

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self, no = 1):
        cards = []
        for i in range(no):
            try:
                cards.append(self.cards.pop(0))
            except IndexError:
                # pop from empty list
                if self.emptyFunc is None:
                    raise NotImplementedError(f"{self} has no emptyFunc!")
                else:
                    self.emptyFunc()
        return cards

    def discard(self, *cards):
        self.discards = []

class InvaderDeck(Deck):
    def __init__(self, cards):
        super().__init__(cards)

    def __repr__(self):
        value = "InvaderDeck:\n"
        for card in self.cards:
            value += f"\t{card}\n"
        return value

    def emptyFunc(self):
        print("You Lose!")

class InvaderCard:
    def __init__(self, *landTypes, escalation=False):
        self.landTypes = landTypes
        self.escalation = escalation

    def __repr__(self):
        escalationString = ""
        if self.escalation:
            escalationString = " ESC"
        if len(self.landTypes) == 1:
            landTypesString = self.landTypes[0]
        else:
            landTypesString = str(self.landTypes)

        return f"{landTypesString}{escalationString}"
