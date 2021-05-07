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


@app.route("/newgame")
def new_game():
    global game
    del game
    return redirect("/")


@app.route("/shuffle")
def shuffle_cards():
    global game
    random.shuffle(game.draw_pile)
    return redirect("/game")

@app.route("/draw")
def draw_card():
    global game
    game.

@app.route("/player_action/<player_idx>", methods=['POST'])
def player_action(player_idx):
    global game
    print(f"player_idx is {player_idx}")
    current_player = game.players[int(player_idx)]
    game.process_turn(current_player, int(player_idx),
                      int(request.form['card_index']))
    print("came back from process turn")
    # if drawpile is empty, then change isTurn false and switch true to next player
    return redirect("/game")


if __name__ == "__main__":
    app.run(debug=True)
