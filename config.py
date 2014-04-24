import os as _os
import ConfigParser as _ConfigParser

cfg = _ConfigParser.ConfigParser()
cfg.read("infrastructure/infrastructure.ini")

address = cfg.get("game", "address")
port = cfg.getint("game", "port")
username = cfg.get("game", "username")
password = cfg.get("game", "password")

aws_access = cfg.get("aws", "access")
aws_secret = cfg.get("aws", "secret")
aws_queue = cfg.get("aws", "queue")

dir_textfiles = cfg.get("locations", "textfiles")
dir_game = cfg.get("locations", "game")
