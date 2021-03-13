class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.color = ""

        colors = {
            1: "Ace",
            11: "Jack",
            12: "Queen",
            13: "King"
        }

        if rank in colors:
            self.color = colors[rank]
        else:
            self.color = str(rank)

    def show_card(self):
        print(f"{self.name} of {self.suit}")


class Deck:
    def __init__(self):
        self.cards = []

        # Populate the cards list -- loop to 52
        for color in ["Blue", "Green", "Purple", "Gold"]:
            for rank in range(1, 14):
                self.cards.append(Card(color, rank))
