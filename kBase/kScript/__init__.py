import cmd
from kScript import apps
class kScript(cmd.Cmd):
	prompt = "k>"
	intro = "kScript V0.0.1 [TIME]"
	doc_header = "k"
	def do_app(self, app):
		app = getattr(apps,"{app}.run()".format(app=app))
	def help_app(self):
		print("Runs an installed application.")
	def do_install(self,app):
		if app in apps.list:
			apps.install(app)
		else:
			self.do_echo("Application not found!")
	def help_install(self):
		print("Installs specified application")
	def do_echo(self,text):
		print(text)
	def help_echo(self):
		print("Echoes text back")
