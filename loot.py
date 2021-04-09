from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'secretpasswordislootgame'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/player_names', methods=['POST'])
def initialize_players():
    print("Got post info")
    print(request.form)
    num_players = request.form['num_players']
    context = {}
    for i in range(num_players):
        context['']
    return render_template("game.html")


if __name__ == "__main__":
    app.run(debug=True)
