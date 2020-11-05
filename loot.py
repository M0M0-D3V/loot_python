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
        self.cards = []

    def new_player(self, name):
        self.players.append(Player(name))
        return self

    def all_players(self):
        for player in self.players:
            print(player.name)
        return self

    def make_drawpile(self):
        card = 1
        self.cards.append(card)
        random.shuffle(self.cards)
        return self


class PirateShips:
    def __init__(self):
        self.card =


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


def start_game():
    the_game = Game()
    the_game.make_drawpile()


game1 = Game()
game1.new_player("monica").new_player("rachel")
game1.all_players()
