from flask import Flask, render_template, request, redirect, session
from game import Player, Card, Game
app = Flask(__name__)
app.secret_key = 'secretpasswordislootgame'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/player_names', methods=['POST'])
def initialize_players():
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
    print(f"player names is {session['player_names']}")
    session['players'][0]['isTurn'] = True
    # [] start new game and apply changes
    session['game'] = {}
    return redirect("/game")


@ app.route("/game")
def start_game():
    game = Game()
    session['game']['draw_pile'] = game.make_drawpile()
    return render_template("game.html", players=session['players'], num=session['num_players'], game=session['game'])


if __name__ == "__main__":
    app.run(debug=True)
