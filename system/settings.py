import os

POSTGRES = {
    'user': os.environ.get('POSTGRESQL_USER'),
    'password': os.environ.get('POSTGRESQL_PASSWORD'),
    'host': os.environ.get('POSTGRESQL_HOST'),
    'port': os.environ.get('POSTGRESQL_PORT'),
    'db': os.environ.get('POSTGRESQL_DB'),
    'version': 15.3
}

MINIO = {
    'host': os.environ.get('MINIO_HOST'),
    'port': os.environ.get('MINIO_API_PORT'),
    'protocol': os.environ.get('MINIO_PROTOCOL'),
    'access_key': os.environ.get('MINIO_ACCESS_KEY'),
    'secret_key': os.environ.get('MINIO_SECRET_KEY'),
}

REDIS = {
    'host': os.environ.get('REDIS_HOST'),
    'port': os.environ.get('REDIS_PORT')
}
