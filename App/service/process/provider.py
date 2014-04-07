#service.data.provider
from service.process.factory.baseProvider import BaseProvider
#TODO: Add textwrap to a query post processor


class Provider(BaseProvider):

    def __init__(self, process_settings):
        BaseProvider.__init__(self, process_settings)

    def handle_process(self):
        self._procProviderFactory.exec_module('var/R/helloWorld.R')
        pass