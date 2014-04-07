#service.process.factory.proc_provider_factories
class ProcProviderFactories(object):
    connection_string = ''

    def __init__(self):
        self.connection = ''
        self._factory = None

    def get_factory(self, process):
        #should instantiate the teradata factory
        tmp = __import__('service.process.factory.'+process.name.lower(), fromlist=[provider_name+'Factory'])
        self._factory = getattr(tmp, provider_name+'Factory')()
        return self._factory