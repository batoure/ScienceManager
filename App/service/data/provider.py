#service.data.provider
from service.data.factory.baseProvider import BaseProvider
#TODO: Add textwrap to a query post processor
from model.workflow import *


class Provider(BaseProvider):

    def __init__(self, log, connectionSettings):
        self._log = log
        #pass to the base connectionSettings
        self._connection_string = ""
        self._connection_settings = connectionSettings
        BaseProvider.__init__(self, self._log, connectionSettings)

    def reserve_next_batch_number(self, workflow, user):
        batch = None
        with self._dbProviderFactory.create_connection(self._connection_settings) as conn:
            conn.connection_string = self._connection_string
            conn.open()
            with conn.create_command() as cmd:
                cmd.command_timeout = 0
                cmd.command_text("""
                                      INSERT INTO WF_BATCH
                                        ( WF_ID, WF_USER)
                                      VALUES
                                        ({workflow} , {user})
                                    """, {'workflow': workflow, 'user': user})
                cmd.execute_non_query()
                cmd.command_text('SELECT BATCH_ID FROM (SELECT MAX(DATE_DT) AS DATE_DT, BATCH_ID FROM WF_BATCH GROUP BY BATCH_ID) AS A',{})
                link_list = cmd.execute_scalar()
                for link in link_list:
                    batch = link
            conn.commit()
            conn.close()
        return batch

    def get_program_details(self, workflow, name):
        with self._dbProviderFactory.create_connection(self._connection_settings) as conn:
            conn.connection_string = self._connection_string
            conn.open()
            with conn.create_command() as cmd:
                cmd.command_timeout = 0
                cmd.command_text("SELECT WF_ID, WF_NAME, WF_FAILURE FROM WF_MASTER_L WHERE WF_NAME = '{workflowname}'", {'workflowname': name})
                for row in cmd.execute_reader():
                    workflow.id, workflow.name, workflow.id = row
            conn.commit()
            conn.close()
        return workflow

    def get_program_actions(self, work_flow_id):
        tasks = []
        with self._dbProviderFactory.create_connection(self._connection_settings) as conn:
            conn.connection_string = self._connection_string
            conn.open()
            with conn.create_command() as cmd:
                cmd.command_timeout = 0
                cmd.command_text("SELECT WF_ID, WF_STEPS_L.STEP_ID, WF_STEPS_L.ACTION_NAME, WF_ACTIONS_TYPES_L.ACTION_TYPE_NAME, WF_STEPS_L.ACTION_TYPE_ID, WF_STEPS_L.ACTION_TXT FROM WF_STEPS_L JOIN WF_ACTIONS_TYPES_L ON WF_STEPS_L.ACTION_TYPE_ID = WF_ACTIONS_TYPES_L.ACTION_TYPE_ID WHERE WF_ID = '{id}'",{'id': work_flow_id})
                for row in cmd.execute_reader():
                    task = Task()
                    wfid, task.number, task.action.name, task.action.type.name, task.action.type.id, task.action.text = row
                    tasks.append(task)
            conn.commit()
            conn.close()
        return  tasks