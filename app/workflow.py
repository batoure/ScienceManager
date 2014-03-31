from service.configuration import Configuration 
from service.database import Database 
import argparse


class Workflow(object):
""" A simple data structure to hold job parameters """
    def __init__(self, log):
        self.log = log
        self.model = None
        self.on_success = None
        self.action = None
        self.on_failure = None
        self.on_success = None
	
	def run(self):
		self.s.config = Configuration('var/cfg.yaml')
		
	def __handle_arguments(self):
		parser = argparse.ArgumentParser(description='Teradata "Science Manager" v0.1 ')
#		parser.add_argument('integers', metavar='N', type=int, nargs='+',
#						   help='an integer for the accumulator')
		parser.add_argument('--program', type=string, 
						   help='set the program to be executed')
		args = parser.parse_args()
		print(args.accumulate(args.integers))

if __name__ == "__main__":
	process = Workflow().run()