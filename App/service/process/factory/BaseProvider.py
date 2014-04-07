#service.process.factory.baseProcess
from service.process.factory.proc_provider_factories import ProcProviderFactories


class BaseProvider(object):
    def __init__(self, process_settings):
        self._procProviderFactory = ProcProviderFactories().get_factory(process_settings)
        pass