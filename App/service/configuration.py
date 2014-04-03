__author__ = 'Batoure'
import yaml
from App.model.configuration import Configuration as Model


class Configuration(object):
    """ A service to import configuration data """
    def __init__(self, file):
        # self.log = log
        self.m = Model()
        self.configfile = yaml.load(open(file))

    def get_logging(self):
        """

        @param self:
        """
        return self.configfile['Logging']

    def set_database_connection(self, connection):
        """

        @param self:
        """
        connection.set_connection_data(self.configfile['ConnectionString'])

        return connection