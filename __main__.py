"""Mummu's MUSH Infrastructure

Usage: infrastructure textfile watch
"""

import docopt

import bot
import queue_watcher

def main(arguments):
    if arguments["textfile"]:
        queue_watcher.main(arguments)

if __name__ == "__main__":
    arguments = docopt.docopt(__doc__, version="Infrastructure v0.1")
    if arguments:
        main(arguments)
