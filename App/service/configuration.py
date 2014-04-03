import yaml
from model.configuration import Configuration as Model


class Configuration(object):
    def __init__(self, file):
        # self.log = log
        self.m = Model()
        self.configfile = yaml.load(open(file))

    def get_logging(self):
        return self.configfile['Logging']

    def set_database_connection(self, connection):
        connection.set_connection_data(self.configfile['ConnectionString'])
        return connection