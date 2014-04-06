#model.connection


class ConnectionSettings(object):

    def __init__(self):
        self.driver = None
        self.dbcname = None
        self.database = None
        self.uid = None
        self.pwd = None
        self.quietmode = None

    def set_connection_data(self, data):
        self.driver = data['Driver']
        self.dbcname = data['Connection']
        self.database = data['Database']
        self.uid = data['User']
        self.pwd = data['Password']
        self.quietmode = 'Yes'