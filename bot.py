import ConfigParser
import telnetlib

cfg = ConfigParser.ConfigParser()
cfg.read("infrastructure.ini")

username = cfg.get_option("game", "username")
password = cfg.get_option("game", )