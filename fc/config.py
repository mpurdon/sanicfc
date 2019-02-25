import logging
import sys

INSTANCE_ID = 'app'
LOG_HANDLER = 'console'
LOG_LEVEL = 'DEBUG'


# class RequestIdFilter(logging.Filter):
#     def filter(self, record):
#         record.request_id = context.get('X-Request-ID')
#         return True


LOGGING_CONFIG = dict(
    version=1,
    disable_existing_loggers=False,

    loggers={
        '': {
            'level': LOG_LEVEL,
            'handlers': ['console']
        },
        'sanic.error': {
            'level': LOG_LEVEL,
            'handlers': ['error_console'],
            'propagate': True,
            'qualname': 'sanic.error'
        },

        'sanic.access': {
            'level': LOG_LEVEL,
            'handlers': ['access_console'],
            'propagate': True,
            'qualname': 'sanic.access'
        }
    },
    handlers={
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'generic',
            'stream': sys.stdout
        },
        'error_console': {
            'class': 'logging.StreamHandler',
            'formatter': 'generic',
            'stream': sys.stderr
        },
        'access_console': {
            'class': 'logging.StreamHandler',
            'formatter': 'access',
            'stream': sys.stdout
        },
    },
    formatters={
        'generic': {
            'format': '%(asctime)s [%(process)d] [%(levelname)s] %(message)s',
            'datefmt': '[%Y-%m-%d %H:%M:%S %z]',
            'class': 'logging.Formatter'
        },
        'access': {
            'format': '%(asctime)s - (%(name)s)[%(levelname)s][%(host)s]: ' +
                      '%(request)s %(message)s %(status)d %(byte)d',
            'datefmt': '[%Y-%m-%d %H:%M:%S %z]',
            'class': 'logging.Formatter'
        },
    }
)
