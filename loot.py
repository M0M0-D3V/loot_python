# OOP practice to make text based LOOT game

# TO DO:
# [] Identify the various classes we need to make
# [] Player class
# [] Player's Hand class
# [] Pirate Ship Cards class
# [] Ranks - 13 total: each color has 2 ones, 4 twos, 4 threes, and 2 fours, and 1 pirate Captain
# [] Colors - blue, green, purple, and gold
# [] Merchant Ships class
# [] Values - 5 twos, 6 threes, 5 fours, 5 fives, 2 sixes, 1 seven, and 1 eight
# [] Identify other global functions to run the game
# [] Build Deck method
# [] Turn phase method
# [] Figure this shit out~ Merchant Seige event....
import random


class Game:
    def __init__(self):
        self.players = []

    def new_player(self, name):
        self.players.append(Player(name))
        return self


class Player:
    def __init__(self, name):
        self.name = name
        self.hand = Hand()
        self.total = 0


class Hand:
    def __init__(self):
        self.cards = []

    def __repr__(self):
        return str(self)


def make_drawpile():
    pass


def start_game():
    drawpile = make_drawpile()
    random.shuffle(drawpile)
