#service.process.factory.baseProcess
from service.process.factory.proc_provider_factories import ProcProviderFactories


class BaseProvider(object):
    def __init__(self, log, process_settings):
        self._log = log
        self._procProviderFactory = ProcProviderFactories(self._log).get_factory(process_settings)
        pass