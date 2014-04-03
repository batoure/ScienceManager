import pyodbc

class Database(object):
    """ A service to establish a database connection and make queries over odbc """
    def __init__(self, log):
        self.log = log
    
    def get_connection(self, ConnStr):
        self.conn = pyodbc.connect('DRIVER={'+ConnStr['Driver']+'};DBCNAME='+ConnStr['Connection']+';database='+ConnStr['Database']+';UID='+ConnStr['User']+';PWD='+ConnStr['Password']+';')
        self.curs = self.conn.cursor()
        return self.curs

    def x_query(self, query):
        for row in self.curs.execute('SELECT WF_ID,WF_NAME,WF_FAILURE FROM WF_MASTER_L WHERE WF_NAME = \''+query['WorkFlowName']+'\';'):
            print(row.WF_ID)