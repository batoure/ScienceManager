from workflow.service.configuration import Configuration
# from .service.database import Database
from workflow.model.object import Object
import argparse
import logging
import logging.config


class Main(object):
    """ A simple data structure to hold job parameters """
    Log = logging
    M = Object
    S = Object
    Args = Object()
    M.Conf = Configuration(file='./workflow/var/cfg.yaml')
    logging.config.dictConfig(M.Conf.get_logging())

    def __init__(self):
        pass

    def run(self):
        self.Log.info('handling arguments')
        self.Log.debug('This should show up in the console')
        self.__handle_arguments()
        self.Log.debug(self.Args.program)

    def __handle_arguments(self):
        parser = argparse.ArgumentParser(description='Teradata "Science Manager" v0.1 ')
        parser.add_argument('--program', type=str, help='set the program to be executed')
        parser.parse_args(namespace=self.Args)


class Error(Exception):
    def __init__(self, m='Workflow error occurred.'):
        self.message = m

    def __str__(self):
        return self.message

if __name__ == "__main__":
    Main().run()