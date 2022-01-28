from flask import Flask, render_template, redirect, url_for, request
import walker_game
from forms.form import ChooseCount, Review
from config import Config

app = Flask(__name__)
app.config.from_object(Config)


@app.route('/', methods=['get', 'post'])
def count():
    global game
    form = ChooseCount()
    count_of_player = form.count_of_player.data
    if form.validate_on_submit():
        game = walker_game.WalkerGame(count_of_player)
        game.start()
        game.player_1.nickname = form.name1.data
        game.player_2.nickname = form.name2.data
        game.player_3.nickname = form.name3.data
        game.player_4.nickname = form.name4.data
        return redirect(url_for('move'))
    return render_template('index.html', form=form)


@app.route('/game/', methods=['GET', 'POST'])  # Скрытые параметры передачи координат клетки
def move():
    if request.method == 'POST':
        index = request.form['index']
        i, j = [int(m) for m in index]
        game.move(i, j)
        return render_template('game.html', game=game)
    return render_template('game.html', game=game)


@app.route('/rules/')
def rules():
    return render_template('rules.html')


@app.route('/review/', methods=['GET', 'POST'])
def review():
    form = Review()
    if form.validate_on_submit():
        name = form.name.data
        browser = form.browser.data
        message = form.message.data
        try:
            rating = int(request.form["rating"])
        except Exception:
            rating = 0
        email = form.email.data
        #  логика базы данных
        return redirect(url_for('review_response', name=name, rating=rating))
    return render_template('review.html', form=form)


@app.route('/review/response/<string:name><int:rating>/', methods=['GET', 'POST'])
def review_response(name, rating):
    return render_template('review-response.html', name=name, rating=rating)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
