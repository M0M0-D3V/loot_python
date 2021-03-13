# OOP practice to make text based LOOT game

# TO DO:
# [x] Identify other global functions to run the game
# [x] Turn phase method
# [] PLAY A TURN PLAYER METHOD
# [] Play a card onto the playfield
# [] Figure this shit out~ Merchant Seige event....
import random

# [x] Player class


class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []  # hand is created from Game.deal()
        self.total = 0
        self.last_played = None

    def play_a_turn(self, game):
        # player should be able to see what cards they have in their hand to decide if they want to play a card vs attack
        self.show_hand()
        # Do an imput for "play merchant ship", "attack merchant"
        # draw_card()
        print("1 - Play a merchant ship")
        print("2 - Attack a merchant ship")
        print("3 - Draw a card")
        move = input("Choose 1, 2, or 3: ")
        # ****************************************
        # figure this out
        if move == "1":
            # should check if player has a merchant ship in hand first
            merchants_in_hand = []
            for card in self.hand:
                if card.card_type == "Merchant Ship":
                    merchants_in_hand.append(card)
            print(f"{self.name} chose to play a merchant ship")
            if len(merchants_in_hand) > 0:
                self.play_merchant_ship(merchants_in_hand, game)
            else:
                print("you don't have a merchant ship in your hand, pick 2 or 3 instead")
                move = input("Choose 2 or 3: ")
        if move == "2":
            merchant_card = "something else"
            pirate = "pick something else"
            self.attack_merchant_ship(merchant_card, pirate, game)
        if move == "3":
            self.draw_card()
        # ****************************************
        # self.draw_card()
        return self

    def draw_card(self):
        print('called the draw_card() function.... but it isn\'t built yet')
        return self

    def play_merchant_ship(self, merchants_in_hand, game):
        print(f"{self.name}, choose a merchant card from your hand")
        for i in range(len(merchants_in_hand)):
            print(
                f"#{i} - {merchants_in_hand[i].card_type} - {merchants_in_hand[i].rank} gold")
        chosen_merchant = merchants_in_hand[int(input(f"choose a number:"))]
        print(
            f"{self.name} plays {chosen_merchant.card_type} - {chosen_merchant.rank}")
        game.play_field['Merchant Ships'].append(chosen_merchant)
        self.last_played = chosen_merchant
        self.hand.remove(chosen_merchant)
        return self

    def attack_merchant_ship(self, merchant, pirate, game):
        print("attacking a merchant ship")
        return self

    def show_hand(self):
        print(f"{self.name}'s hand:")
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
        # each to the play_fiend append should be a nested object with a lit of object attacking pirates which
        self.play_field = {
            'Merchant Ships':
            [

            ],
            'Players Attacking':
                [
                    {'Player Name': ""},
            ]
        }
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

    def turn_order(self):
        # maybe shuffle this list later?
        print(f"The order of play will be:")
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

    def setup(self):
        self.number_of_players = input("Number of Players: ")
        self.get_players()
        self.all_players()
        self.make_drawpile()
        # self.get_cards_in_drawpile()
        random.shuffle(self.draw_pile)
        random.shuffle(self.draw_pile)
        print("*"*20)
        self.get_cards_in_drawpile()
        self.deal()

    def start(self):
        this_game = self
        self.turn_order()
        # while loop instead
        for player in self.players:
            if len(self.draw_pile) > 0:
                print(f"{player.name}'s turn...")
                something = player.play_a_turn(this_game)
                print(f"got something {something}")
                print(self.play_field)
        return self


game1 = Game()
game1.setup()
game1.start()
