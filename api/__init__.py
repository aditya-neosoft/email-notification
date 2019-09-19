from django.db import connection

if connection.introspection.table_names():
    default_app_config = 'api.apps.ApiConfig'
