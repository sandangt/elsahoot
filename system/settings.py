import os

POSTGRES = {
    'user': os.environ.get('POSTGRESQL_USER'),
    'password': os.environ.get('POSTGRESQL_PASSWORD'),
    'host': os.environ.get('POSTGRESQL_HOST'),
    'port': os.environ.get('POSTGRESQL_PORT'),
    'db': os.environ.get('POSTGRESQL_DB'),
    'version': 15.3
}

REDIS = {
    'host': os.environ.get('REDIS_HOST'),
    'port': os.environ.get('REDIS_PORT')
}
