from storages.backends.azure_storage import AzureStorage

class AzureMediaStorage(AzureStorage):
    account_name = 'msptestportalstatic' # Must be replaced by your <storage_account_name>
    account_key = 'yqJHEHEVwFdQhuiDj7CgLElZob2JQ3v1GNPAyd6oQfclIq5W0KjKyD2V+EfcUnXjTJeEQOYfTqfBsF+N/yZuGA==' # Must be replaced by your <storage_account_key>
    azure_container = 'media'
    expiration_secs = None

class AzureStaticStorage(AzureStorage):
        account_name = 'msptestportalstatic' # Must be replaced by your storage_account_name
        account_key = 'yqJHEHEVwFdQhuiDj7CgLElZob2JQ3v1GNPAyd6oQfclIq5W0KjKyD2V+EfcUnXjTJeEQOYfTqfBsF+N/yZuGA==' # Must be replaced by your <storage_account_key>
        azure_container = 'static'
        expiration_secs = None
