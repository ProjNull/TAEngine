import os
from time import sleep

from modules.game import Game
from modules.ui import printLogo as ui_logo
from modules.ui import printUi as ui_selector


def find_json_files():
    json_files = []
    cwd = os.getcwd()
    i = 0
    for root, dirs, files in os.walk(cwd):
        for file in files:
            if file.endswith(".taj"):
                json_files.append(os.path.join(root, file))
        i += 1
        if i >= 512:
            print("Terminated search for taj files, as it went too deep.")
            break
    names = []
    for i in json_files:
        names.append(i.replace("\\", "/").split("/")[-1])
    return [json_files, names]


GAMES = find_json_files()

while 1:
    # Main Loop
    ui_logo()
    sleep(1)
    try:
        game_file = ui_selector(
            "Please select an adventure file", GAMES[1], clear_screen=True
        )
    except KeyboardInterrupt:
        break
    except EOFError:
        exit(0)
    game = GAMES[0][game_file]
    # Run game
    g = Game(game)
    try:
        g()
    except EOFError:
        pass
    except KeyboardInterrupt:
        pass
print("Goodbye!")
