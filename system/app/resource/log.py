import logging.config

from app.settings import APP_LOGGING_CONFIG

logging.config.dictConfig(APP_LOGGING_CONFIG)


def logger_factory(name: str):
    return logging.getLogger(name)
