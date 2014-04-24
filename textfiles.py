import os
import subprocess

import bot
import config

mkindx = os.path.join(config.dir_game, "mkindx")

def updated():
    for filename in os.listdir(config.textfiles):
        if filename.endswith(".txt"):
            print filename

