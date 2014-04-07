#service.job
from service.data.provider import Provider as dataSource
from service.process.provider import Provider as Process


class Job(object):
    """ A service to execute external applications """
    def __init__(self, conn, log):
        self._source = dataSource(conn)
        self._log = log

    def get_job_details(self, name):
        self._source.get_program_details(name)
        pass

    def setup_job(self, job):
        self._source.reserve_next_batch_number(self._log, 1, 1)
        pass

    def process_job_items(self, tasks):
        for task in tasks:
            proc = Process(task.action.type)
            proc.handle_process(task.action.text)
        pass

    def _execute_job(self, job):

        pass