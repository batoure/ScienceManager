#service.workflow
from service.data.provider import Provider


class Workflow(object):

    def __init__(self, conn, log):
        self.__source = Provider(conn)
        self.__log = log

    def get_job_details(self, name):
        self.__source.get_program_details(name)
        pass

    def setup_job(self, job):
        self.__source.reserve_next_batch_number(self.__log, 1, 1)
        pass