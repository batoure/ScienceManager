#service.data.factory.teradata
import pyodbc


class TeradataFactory(object):

    def __init__(self):
        self.connection = None
        self._connection_settings = None

    def __enter__(self):
        return self

    def __exit__(self,  type,  value,  traceback):
        return False

    @staticmethod
    def _connection_string(connection_string):
        return 'DRIVER={'+connection_string.driver+'};DBCNAME='+connection_string.dbcname+';database='+connection_string.database+';UID='+connection_string.uid+';PWD='+connection_string.pwd+';'

    def create_connection(self, connection_settings):
        self._connection_settings = connection_settings
        return self

    def open(self):
        try:
            self.connection = pyodbc.connect(self._connection_string(self._connection_settings))
        except:
            raise
        else:
            return True

    def close(self):
        #execute open connection in the teradata factory
        pass

    def commit(self):
        #execute open connection in the teradata factory
        pass

    def create_command(self):
        return Command(self.connection)


class Command(object):

    def __init__(self, connection):
        self.connection = connection
        self.command_timeout = 0
        self.__command_text = None

    def __enter__(self):
        return self

    def command_text(self, text, var, log):
        self.__command_text = text.format(**var)
        log.info(self.__command_text)

    def __exit__(self,  type,  value,  traceback):
        return False

    def execute_scalar(self):
        return self.connection.execute(self.__command_text).fetchone()

    def execute_non_query(self):
        return self.connection.execute(self.__command_text).rowcount

    def execute_reader(self):
        return self.connection.execute(self.__command_text).fetchall()
