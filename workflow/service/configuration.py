__author__ = 'Batoure'
import yaml
from ..model.configuration import Configuration as Model


class Configuration(object):
    """ A service to import configuration data """
    def __init__(self, log, file):
        self.log = log
        self.m = Model()
        self.configfile = yaml.load(open(file))

    def get_database_connection(self):
        """

        @param self:
        """
        pass