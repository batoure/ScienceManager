from .service.configuration import Configuration
# from .service.database import Database
import argparse
import logging


class Workflow(BaseException):
    """ A simple data structure to hold job parameters """
    Log = logging.basicConfig(filename='/bin/example.log', level=logging.DEBUG)
    S = None
    S.Configuration = Configuration(file='var/cfg.yaml', log=Log)

    def __init__(self):
        self.model = None
        self.on_success = None
        self.action = None
        self.on_failure = None
        self.on_success = None
        self.s = None

    def run(self):
        self.Log.info('handling arguments')
        self.__handle_arguments()


    @staticmethod
    def __handle_arguments():
        parser = argparse.ArgumentParser(description='Teradata "Science Manager" v0.1 ')
        #		parser.add_argument('integers', metavar='N', type=int, nargs='+',
        #						   help='an integer for the accumulator')
        parser.add_argument('--program', type=str,
                            help='set the program to be executed')
        args = parser.parse_args()
        print(args.accumulate(args.integers))


class Error(Exception):
    def __init__(self, m='Workflow error occurred.'):
        self.message = m

    def __str__(self):
        return self.message

if __name__ == "__main__":
    Workflow().run()