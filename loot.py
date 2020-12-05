# OOP practice to make text based LOOT game

# TO DO:
# [x] Identify the various classes we need to make
# [x] Player class
# [] Cards class
# [x] Ranks - 13 total: each color has 2 ones, 4 twos, 4 threes, and 2 fours, and 1 pirate Captain
# [x] Colors - blue, green, purple, and gold
# [x] Merchant Ships class
# [x] Values - 5 twos, 6 threes, 5 fours, 5 fives, 2 sixes, 1 seven, and 1 eight
# [x] Identify other global functions to run the game
# [x] Build Deck method
# [] Turn phase method
# [] Figure this shit out~ Merchant Seige event....
import random


# [x] Player class
class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.total = 0
        self.merchant_ships = []

    def draw_card(self):
        pass

    def play_merchant_ship(self, merchant_card):
        pass

    def attack_merchant_ship(self, merchant, pirate):
        pass

    def show_hand(self):
        for card in self.hand:
            if card.card_type == "Merchant Ship":
                print(f"{card.card_type} - {card.rank}")
            if card.card_type == "Admiral":
                print(f"{card.card_type}")
            if card.card_type == "Pirate Ship":
                print(f"{card.card_type} - {card.color} {card.rank}")
        return self


class Card:
    def __init__(self, card_type, color, rank):
        self.card_type = card_type
        self.color = color
        self.rank = rank

    def show_card(self):
        if self.rank == "Admiral":
            print(f"{self.rank}")
        if self.card_type == "Merchant Ship":
            print(f"{self.card_type} of {self.rank} value")
        else:
            print(f"{self.rank} of {self.color}")
        return self


class Game:
    def __init__(self):
        self.number_of_players = 0
        self.players = []
        self.draw_pile = []
        self.play_field = []
        self.discard_pile = []

    def get_players(self):
        for i in range(int(self.number_of_players)):
            name = input(f'Player {i+1} Enter your name:')
            self.players.append(Player(name))
        return self

    def all_players(self):
        print(f'{self.number_of_players} players:')
        for player in self.players:
            print(player.name)
        return self

    def make_drawpile(self):
        # ***************************
        # first append all the pirate cards
        # [x] Ranks - 13 total: each color has 2 ones, 4 twos, 4 threes, and 2 fours, and 1 pirate Captain
        card_type = "Pirate Ship"
        for color in ["Blue", "Green", "Purple", "Gold"]:
            for i in range(2):
                rank = 1
                self.draw_pile.append(Card(card_type, color, rank))
            for i in range(4):
                rank = 2
                self.draw_pile.append(Card(card_type, color, rank))
            for i in range(4):
                rank = 3
                self.draw_pile.append(Card(card_type, color, rank))
            for i in range(2):
                rank = 4
                self.draw_pile.append(Card(card_type, color, rank))
            self.draw_pile.append(Card(card_type, color, "Captain"))
        # ***************************
        # next append all the merchant ships
        # [x] Values - 5 twos, 6 threes, 5 fours, 5 fives, 2 sixes, 1 seven, and 1 eight
        card_type = "Merchant Ship"
        color = None
        for i in range(5):
            rank = 2
            self.draw_pile.append(Card(card_type, color, rank))
        for i in range(6):
            rank = 3
            self.draw_pile.append(Card(card_type, color, rank))
        for i in range(5):
            rank = 4
            self.draw_pile.append(Card(card_type, color, rank))
        for i in range(5):
            rank = 5
            self.draw_pile.append(Card(card_type, color, rank))
        self.draw_pile.append(Card(card_type, color, 6))
        self.draw_pile.append(Card(card_type, color, 6))
        self.draw_pile.append(Card(card_type, color, 7))
        self.draw_pile.append(Card(card_type, color, 8))
        # ******************************
        # Add the Admiral
        self.draw_pile.append(Card("Admiral", None, None))
        # ******************************
        return self

    def get_cards_in_drawpile(self):
        for card in self.draw_pile:
            if card.card_type == "Merchant Ship":
                print(f"{card.card_type} - {card.rank}")
            if card.card_type == "Admiral":
                print(f"{card.card_type}")
            if card.card_type == "Pirate Ship":
                print(f"{card.card_type} - {card.color} {card.rank}")
        return self

    def deal(self):
        for i in range(6):
            for player in self.players:
                popped = self.draw_pile.pop()
                player.hand.append(popped)
        return self

    def start(self):
        self.number_of_players = input("Number of Players: ")
        self.get_players()
        self.all_players()
        self.make_drawpile()
        # self.get_cards_in_drawpile()
        random.shuffle(self.draw_pile)
        print("*"*20)
        self.get_cards_in_drawpile()
        self.deal()


game1 = Game()
game1.start()
