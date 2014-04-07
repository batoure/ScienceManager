#service.job
from service.data.provider import Provider as dataSource
from service.process.provider import Provider as Process


class Job(object):
    """ A service to execute external applications """
    def __init__(self, log, conn):
        self._log = log
        self._source = dataSource(self._log, conn)

    def get_job_details(self, workflow, name):
        return self._source.get_program_details(workflow, name)

    def register_job(self, workflow_id, user_id):
        return self._source.reserve_next_batch_number(workflow_id, user_id)

    def setup_job(self, workflow_id):
        return self._source.get_program_actions(workflow_id)

    def process_job_items(self, tasks):
        for task in tasks:
            proc = Process(self._log, task.action.type)
            proc.handle_process(task.action.text)
        pass
