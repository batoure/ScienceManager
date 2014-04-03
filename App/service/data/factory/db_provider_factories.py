class DbProviderFactories(object):
    connection_string = ''

    def __init__(self):
        self.connection = ''
        self.__factory = None

    def get_factory(self, provider_name):
        #should instantiate the teradata factory
        tmp = __import__('App.service.data'+provider_name.lower()+'_factory', fromlist=[provider_name+'Factory'])
        self._factory = getattr(tmp, provider_name+'Factory')()
        return self._factory

