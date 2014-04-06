#service.data.provider
from service.data.factory.baseProvider import BaseProvider
#TODO: Add textwrap to a query post processor

class Provider(BaseProvider):

    def __init__(self, connectionSettings):
        #pass to the base connectionSettings
        self._connection_string = ""
        self._connection_settings = connectionSettings
        BaseProvider.__init__(self, connectionSettings)

    def reserve_next_batch_number(self, log, workflow, user):
        batch = None
        with self._dbProviderFactory.create_connection(self._connection_settings) as conn:
            conn.connection_string = self._connection_string
            conn.open()
            with conn.create_command() as cmd:
                cmd.command_timeout = 0
                cmd.command_text('SELECT BATCH_ID+1 FROM (SELECT MAX(DATE_DT) AS DATE_DT, BATCH_ID FROM WF_BATCH GROUP BY BATCH_ID) AS A', {}, log)
                link_list = cmd.execute_scalar()
                for link in link_list:
                    batch = link
                cmd.command_text("""
                                      INSERT INTO WF_BATCH
                                        (BATCH_ID,  WF_ID, WF_USER)
                                      VALUES
                                        ({batch} , {workflow} , {user})
                                    """, {'batch': batch, 'workflow': workflow, 'user': user}, log)
                cmd.execute_non_query()
            conn.commit()
            conn.close()
        return batch

    def get_program_details(self, name):
        with self._dbProviderFactory.create_connection(self._connection_settings) as conn:
            conn.connection_string = self._connection_string
            conn.open()
            with conn.create_command() as cmd:
                cmd.command_timeout = 0
                cmd.command_text('SELECT WF_ID,WF_NAME,WF_FAILURE FROM WF_MASTER_L WHERE WF_NAME = "{workflowname}"', {'workflowname':name})
                link_list = cmd.execute_scalar()
                for link in link_list:
                    batch = link
            conn.commit()
            conn.close()
        return batch

    def get_program_actions(self, tasks):
        with self._dbProviderFactory.create_connection(self._connection_settings) as conn:
            conn.connection_string = self._connection_string
            conn.open()
            with conn.create_command() as cmd:
                cmd.command_timeout = 0
                cmd.command_text = 'SELECT	WF_ID, STEP_ID, ACTION_NAME, ACTION_TYPE_ID, ACTION_TXT FROM WF_STEPS_L WHERE WF_ID = 1'
                rd = cmd.execute_reader()
                c = 0
                for task in rd:
                    tasks[c] = task
                    c += 1
            conn.commit()
            conn.close()
        return  tasks