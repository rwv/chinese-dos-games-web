import inspect
import json
import os

root = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))

with open(os.path.join(root, 'static', 'games', 'games.json'), encoding='utf8') as f:
    content = f.read()
    game_infos = json.loads(content)

game_infos_with_cover = list()
for identifier, game_info in game_infos['games'].items():
    if 'coverFilename' in game_info.keys():
        game_infos_with_cover.append(game_info)
