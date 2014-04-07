#service.process.factory.proc_provider_factories
class ProcProviderFactories(object):

    def __init__(self):
        self._factory = None

    def get_factory(self, process):
        #should instantiate the teradata factory
        if self._factory is None:
            tmp = __import__('service.process.factory.'+process.name.lower(), fromlist=[process.name+'Factory'])
            self._factory = getattr(tmp, process.name+'Factory')()
        return self._factory