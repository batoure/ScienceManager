#service.data.provider
from service.process.factory.baseProvider import BaseProvider
#TODO: Add textwrap to a query post processor


class Provider(BaseProvider):

    def __init__(self, log, process_settings):
        self._log = log
        BaseProvider.__init__(self, self._log, process_settings)

    def handle_process(self, process):
        self._procProviderFactory.exec_module(process)
        pass