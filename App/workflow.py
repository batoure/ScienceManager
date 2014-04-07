#workflow
import sys
##python libraries
import argparse
import logging
import logging.config
##
## Internal libraries
from service.configuration import Configuration
from service.job import Job
from model.object import Object
from model.connection import ConnectionSettings
from model.workflow import *


class Program(object):
    """ A simple data structure to hold job parameters """
    Log = logging
    M = Object()
    S = Object()
    Args = Object()
    M.Workflow = Workflow()
    M.Tasks = []
    S.Conf = Configuration(file='./var/cfg.yaml')
    logging.config.dictConfig(S.Conf.get_logging())

    def __init__(self):
        pass

    def main(self):
        self._handle_arguments()
        program = None
        program = self.Args.program
        if program is not None:
            self.M.conn = self.S.Conf.set_database_connection(ConnectionSettings())
            self.S.job = Job(self.Log, self.M.conn)
            #
            self.M.Workflow = self.S.job.get_job_details(self.M.Workflow, self.Args.program)
            #
            self.M.Workflow.batch_id = self.S.job.register_job(1, 1)
            #
            self.M.Workflow.tasks = self.S.job.setup_job(self.M.Workflow.id)
            #
            self.S.job.process_job_items(self.M.Workflow.tasks)

    def _handle_arguments(self):
        self.Log.info('handling arguments')
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