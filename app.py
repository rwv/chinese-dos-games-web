from flask import Flask
from flask import render_template, redirect, url_for, make_response, request

from game_infos import game_infos, game_infos_with_cover
import json

number_to_show_on_index = 42

app = Flask(__name__)


@app.route('/')
def index():
    game_infos_to_show = game_infos_with_cover[:number_to_show_on_index - 1]
    return render_template('index-imgs.html', game_infos=game_infos_to_show, game_count=len(game_infos['games']))


@app.route('/about')
def about():
    return render_template('about.html', games=game_infos['games'])


@app.route('/games/')
def games():
    return render_template('games.html', games=game_infos['games'])


@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('q')
    if query is None:
        return render_template('error.html'), 404
    search_games = dict()
    for identifier, value in game_infos['games'].items():
        if query in value['name']['zh-Hans']:
            search_games[identifier] = value
    return render_template('search.html', games=search_games, query=query)


@app.route('/games/<identifier>/')
def game(identifier):
    game_info = game_infos["games"][identifier]
    return render_template('game.html', game_info=game_info)


@app.route('/games/<identifier>/logo/emularity_color_small.png')
def emularity_logo(identifier):
    return redirect(url_for('static', filename='emularity/emularity_color_small.png'), code=301)


if __name__ == '__main__':
    app.run(debug=True)
