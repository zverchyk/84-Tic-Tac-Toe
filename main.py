from flask import Flask, redirect, render_template, request, jsonify, session, json, url_for
from tictactoe import TicTacToe


app = Flask(__name__)
app.secret_key = 'your_secret_key'
game = TicTacToe()
  
@app.route('/', methods=['GET', "POST"])
def main():
    end_game = session.get('end_game', False)
    current_player = session.get('current_player', False)
    if request.method == "POST":
        board = session.get('board', 0)
        data = request.get_json()
        if data:
            move = int(data['key'])-1
            current_player = data['current_player']
            board, end_game, result = game.play_game(move=move, current_player=current_player, board=board)
            session['result'] = result
            session['board'] = board
            session['current_player'] = current_player
            session['end_game'] = end_game

    data = {"clean_list": True}
    return render_template('index.html', data_json=json.dumps(data))



@app.route('/data')
def data():
    end_game = session.get('end_game', False)
    result = session.get('result', False)
    data={"message": end_game, "result": result}
    return jsonify(data)

@app.route('/restart')
def restart():
    session.clear()
    return redirect(url_for('main'))

if __name__ == "__main__":
    app.run(debug=True)






