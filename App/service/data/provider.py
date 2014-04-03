from App.service.data.factory.baseProvider import BaseProvider


class Provider(BaseProvider):

    def __init__(self, connectionSettings):
        #pass to the base connectionSettings
        self._connection_string = ""
        self._connection_settings = connectionSettings
        BaseProvider.__init__(self, connectionSettings)

        pass

    def reserve_next_batch_number(self):
        with self._dbProviderFactory.create_connection(self._connection_settings) as conn:
            conn.connection_string = self._connection_string
            conn.open()
            with conn.create_command() as cmd:
                cmd.command_timeout = 0
                cmd.command_text = 'SELECT WF_ID,WF_NAME,WF_FAILURE FROM WF_MASTER_L'
                batch = cmd.execute_scalar()
            conn.commit()
            conn.close()
        return batch

    def get_connection(self):
        pass

    def x_query(self):
        pass