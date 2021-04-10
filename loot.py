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
    return render_template('index.html')


@app.route('/player_names', methods=['POST'])
def initialize_players():
    global game
    game.make_drawpile()
    random.shuffle(game.draw_pile)
    random.shuffle(game.draw_pile)
    print("Got post info")
    print(request.form)
    session['num_players'] = int(request.form['num_players'])
    print(f"number of players is.... {session['num_players']}")
    # [x] store players in session
    session['players'] = []
    for i in range(1, session['num_players']+1):
        session['players'].append(
            {
                'player_name': request.form['player_name_' + str(i)],
                'isTurn': False,
            })
    session['players'][0]['isTurn'] = True
    print(f"player info is {session['players']}")
    # [] start new game and apply changes
    return redirect("/game")


@ app.route("/game")
def start_game():
    global game
    return render_template("game.html", players=session['players'], num=session['num_players'], draw_pile=game.draw_pile)


if __name__ == "__main__":
    app.run(debug=True)
