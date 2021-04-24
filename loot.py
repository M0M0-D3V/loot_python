from game import Game
from flask import Flask, render_template, request, redirect, session
from game import Player, Card, Game
import random
app = Flask(__name__)
app.secret_key = 'secretpasswordislootgame'

global game
game = Game()


@app.route('/')
def index():
    global game
    if 'game' not in locals() or 'game' not in globals():
        game = Game()
    return render_template('index.html')


@app.route('/player_names', methods=['POST'])
def initialize_players():
    # [x] start new game and apply changes
    global game
    game.make_drawpile()
    random.shuffle(game.draw_pile)
    random.shuffle(game.draw_pile)
    print("Got post info")
    print(request.form)
    game.number_of_players = int(request.form['num_players'])
    session['num_players'] = game.number_of_players
    # [x] call create player
    game.get_players(request.form)
    print(f"printing players from game info: {game.players}")
    # [x] store players in session
    game.players[0].isTurn = True
    # [x] give players hand
    game.deal()
    return redirect("/game")


@app.route("/game")
def start_game():
    global game
    return render_template("game.html", players=game.players, num=session['num_players'], draw_pile=game.draw_pile, play_field=game.play_field, discard_pile=game.discard_pile)


@app.route("/shuffle")
def shuffle_cards():
    global game
    random.shuffle(game.draw_pile)
    return redirect("/game")


@app.route("/newgame")
def new_game():
    global game
    del game
    return redirect("/")


@app.route("/player_action/<player_idx>", methods=['POST'])
def player_action(player_idx):
    global game
    current_player = game.players[int(player_idx)]
    card_idx = int(request.form['card_index'])
    card_played = current_player.hand[card_idx]
    print(f"card number was: {request.form['card_index']}")
    print(f"player {current_player.name} played card {card_played.card_type}")
    # check if card played is merchant or pirate
    if card_played.card_type == "Merchant Ship":
        removed_card = current_player.hand.pop(card_idx)
        game.play_field.append(removed_card)
    elif card_played.card_type == "Pirate Ship":
        # check if play_field has a merchant ship to attack
        pass
    # pop from hand the index received from form
    # add the return from pop into play_field
    # check if len(draw_pile) > 0 then prompt player to draw card
    # redirect to draw card method
    # if drawpile is empty, then change isTurn false and switch true to next player
    return redirect("/game")


if __name__ == "__main__":
    app.run(debug=True)
