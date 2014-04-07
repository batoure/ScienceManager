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
            self.S.job = Job(self.M.conn, self.Log)
            #
            #self.S.job.get_job_details(self.Args.program)
            #
            #self.S.job.setup_job('hello')
            #M.Tasks should be set by setup job
            self.M.Tasks = set_tasks()
            #
            self.S.job.process_job_items(self.M.Tasks)

    def _handle_arguments(self):
        self.Log.info('handling arguments')
        parser = argparse.ArgumentParser(description='Teradata "Science Manager" v0.1 ')
        parser.add_argument('-p', '--program', help='set the program to be executed')
        parser.add_argument('-l', '--list', help='get a list of available programs')
        if len(sys.argv) == 1:
            parser.print_help()
            sys.exit(1)
        parser.parse_args(namespace=self.Args)


def set_tasks():
    tasks = []
    task = Task()
    task.number = 1
    task.action.name = 'R-hello-world'
    task.action.type.name = 'r'
    task.action.type.id = 2
    task.action.text = 'var/R/helloWorld.R'
    tasks.append(task)
    task = Task()
    task.number = 2
    task.action.name = 'R-hello-world2'
    task.action.type.name = 'r'
    task.action.type.id = 2
    task.action.text = 'var/R/helloWorld.R'
    tasks.append(task)
    return tasks


class Error(Exception):
    def __init__(self, m='Workflow error occurred.'):
        self.message = m

    def __str__(self):
        return self.message

if __name__ == "__main__":
    Program().main()