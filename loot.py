# OOP practice to make text based LOOT game

# TO DO:
# [] Identify the various classes we need to make
# [] Player class
# [] Cards class
# [] Ranks - 13 total: each color has 2 ones, 4 twos, 4 threes, and 2 fours, and 1 pirate Captain
# [] Colors - blue, green, purple, and gold
# [] Merchant Ships class
# [] Values - 5 twos, 6 threes, 5 fours, 5 fives, 2 sixes, 1 seven, and 1 eight
# [] Identify other global functions to run the game
# [] Build Deck method
# [] Turn phase method
# [] Figure this shit out~ Merchant Seige event....
import random


class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.total = 0

    def draw_card(self):
        pass

    def play_merchant_ship(self, merchant_card):
        pass

    def attack_merchant_ship(self, merchant, pirate):
        pass


class Card:
    def __init__(self, card_type, color, rank):
        self.card_type = card_type
        self.color = color
        self.rank = rank

    def show_card(self):
        print(f"{self.rank} of {self.color}")


class Game:
    def __init__(self, number_of_players):
        self.number_of_players = number_of_players
        self.players = []
        self.draw_pile = []
        self.discard_pile = []

    def get_players(self):
        for i in range(self.number_of_players):
            name = input(f'Player {i+1} Enter your name:')
            self.players.append(Player(name))
        return self

    def all_players(self):
        print(f'{self.number_of_players} players:')
        for player in self.players:
            print(player.name)
        return self

    def make_drawpile(self):
        # first append all the pirate cards
        for color in ["Blue", "Green", "Purple", "Gold"]:
            self.draw_pile.append(Card(card_type, color, rank))
        # next append all the merchant ships
        random.shuffle(self.draw_pile)
        return self

    def pass_starting_cards(self):
        pass

    def start(self):
        self.get_players()
        self.all_players()
        # self.make_drawpile()
        # self.pass_starting_cards()
        # class Hand:
        #     def __init__(self):
        #         self.cards = []

        # def __repr__(self):
        #     return str(self)


game1 = Game(2)
game1.start()
# game1.new_player("monica").new_player("rachel")
# game1.all_players()
