import ConfigParser
import telnetlib

import config

telnet = telnetlib.Telnet(config.address, config.port)
telnet.read_very_eager() # dump loading screen
telnet.write("connect %s %s\n" % (config.username, config.password))

def send():
    pass

