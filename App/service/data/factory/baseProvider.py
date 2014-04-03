from service.data.factory.db_provider_factories import DbProviderFactories


class BaseProvider(object):
    def __init__(self, connection_settings):
        self._dbProviderFactory = DbProviderFactories().get_factory(connection_settings.driver)
        # if connection_settings.ProviderName == 'SqlClient':
        #     self._dbPlatform = DatabasePlatform.SqlServer
        # elif connection_settings.ProviderName == 'Teradata':
        #     self._dbPlatform = DatabasePlatform.TeraData
        # self._connectionString = connection_settings.ConnectionString

