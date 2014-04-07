#service.data.provider
from service.process.factory.baseProvider import BaseProvider
#TODO: Add textwrap to a query post processor


class Provider(BaseProvider):

    def __init__(self, process_settings):
        BaseProvider.__init__(self, process_settings)

    def dosomething(self, log):
        pass

    def get_program_details(self, name):
        pass

    def get_program_actions(self, tasks):
        pass