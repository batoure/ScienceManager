#workflow
import sys
##python libraries
import argparse
import logging
import logging.config
##
## Internal libraries
from service.configuration import Configuration
from service.workflow import Workflow
from model.object import Object
from model.connection import ConnectionSettings


class Program(object):
    """ A simple data structure to hold job parameters """
    Log = logging
    M = Object()
    S = Object()
    Args = Object()
    M.Conf = Configuration(file='./var/cfg.yaml')
    logging.config.dictConfig(M.Conf.get_logging())

    def __init__(self):
        pass

    def main(self):
        self._handle_arguments()
        self.Log.info('handling arguments')
        self.Log.debug('This should show up in the console')
        self.M.conn = self.M.Conf.set_database_connection(ConnectionSettings())
        self.Log.debug(self.Args.program)

    def _handle_arguments(self):
        parser = argparse.ArgumentParser(description='Teradata "Science Manager" v0.1 ')
        parser.add_argument('-p', '--program', help='set the program to be executed')
        parser.add_argument('-l', '--list', help='get a list of available programs')
        if len(sys.argv) == 1:
            parser.print_help()
            sys.exit(1)
        parser.parse_args(namespace=self.Args)


class Error(Exception):
    def __init__(self, m='Workflow error occurred.'):
        self.message = m

    def __str__(self):
        return self.message

if __name__ == "__main__":
    Program().main()