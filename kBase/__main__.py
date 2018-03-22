import configparser
config = configparser.ConfigParser()
config.read("config.ini")
if config["settings"].getboolean("graphical"):
	import kWindow
	kWindow.run()
else:
	import Konsole
	Konsole.run()