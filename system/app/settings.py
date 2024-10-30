from enum import Enum

# region APP info
APP_TITLE = 'Elsa hoot API'
APP_SWAGGER_URL = '/documentation'
APP_REDOC_URL = '/documentation/redoc'
APP_VERSION = '0.2.0'
APP_TIMEZONE = 'UTC'
APP_METADATA = []
APP_LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(asctime)s %(module)s %(message)s'
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'DEBUG',
            'formatter': 'verbose',
        },
        'file': {
            'class': 'logging.FileHandler',
            'filename': 'app.log',
            'level': 'INFO',
            'formatter': 'verbose',
        },
        'rotating_file': {
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'app_rotating.log',
            'maxBytes': 5 * 1024 * 1024,  # 5 MB
            'backupCount': 2,
            'level': 'INFO',
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'elsa': {
            'handlers': ['console'],
            'formatters': ['simple'],
            'level': 'DEBUG'
        }
    }
}
# endregion

# region Middleware config
CORS_ALLOWED_ORIGINS = (
    'http://localhost:49001',
    'http://localhost:49002'
)
CORS_ALLOWED_METHODS = ['*']
# endregion


class MemcacheDB(Enum):
    INTERNAL = '0'
    API_COLLECTING = '1'
