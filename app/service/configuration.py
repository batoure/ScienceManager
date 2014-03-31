import yaml
from model.configuration import Configuration as model

class Configuration(object):
""" A service to import configuration data """
    def __init__(self, log,file):
        self.log = log
		self.m = model()
		cfgfile = yaml.load(open(file))
		
	def get_database_connection(self):
		pass
	
	