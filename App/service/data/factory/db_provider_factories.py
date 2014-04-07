#service.data.factory.db_provider_factories
class DbProviderFactories(object):
    connection_string = ''

    def __init__(self, log):
        self._log = log
        self.connection = ''
        self._factory = None

    def get_factory(self, provider_name):
        #should instantiate the teradata factory
        if self._factory is None:
            tmp = __import__('service.data.factory.'+provider_name.lower(), fromlist=[provider_name+'Factory'])
            self._factory = getattr(tmp, provider_name+'Factory')(self._log)
        return self._factory

