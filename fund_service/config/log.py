import sys


def get_log_config(config):
    default_level = 'DEBUG' if config.DEBUG else 'INFO'

    return {
        'version': 1,
        'disable_existing_loggers': False,
        'loggers': {
            'sanic.root': {
                'level': default_level,
                'handlers': ['console'],
            },
            'sanic.error': {
                'level':  default_level,
                'handlers': ['error_console'],
                'propagate': True,
                'qualname': 'sanic.error',
            },
            'sanic.access': {
                'level': default_level,
                'handlers': ['access_console'],
                'propagate': True,
                'qualname': 'sanic.access',
            },
            'app': {
                'level': default_level,
                'handlers': ['app_console'],
                'propagate': True,
                'qualname': 'app',
            },
        },
        'handlers': {
            'console': {
                'class': 'logging.StreamHandler',
                'formatter': 'generic',
                'stream': sys.stdout,
            },
            'error_console': {
                'class': 'logging.StreamHandler',
                'formatter': 'generic',
                'stream': sys.stderr,
            },
            'access_console': {
                'class': 'logging.StreamHandler',
                'formatter': 'access',
                'stream': sys.stdout,
            },
            'access_file': {
                'class': 'logging.handlers.RotatingFileHandler',
                'formatter': 'access',
                'filename': '{}/access.log'.format(config.DATA_PATH),
                'maxBytes': 10 * 1024 * 1024,
            },
            'app_console': {
                'class': 'logging.StreamHandler',
                'formatter': 'generic',
                'stream': sys.stdout,
            },
            'app_file': {
                'class': 'logging.handlers.RotatingFileHandler',
                'formatter': 'generic',
                'filename': '{}/app.log'.format(config.DATA_PATH),
                'maxBytes': 10 * 1024 * 1024,
            },
        },
        'formatters': {
            'generic': {
                'format': '%(asctime)s [%(process)d] [%(levelname)s] %(message)s',
                'datefmt': '[%Y-%m-%d %H:%M:%S %z]',
                'class': 'logging.Formatter',
            },
            'access': {
                'format': '%(asctime)s - (%(name)s)[%(levelname)s][%(host)s]: '
                + '%(request)s %(message)s %(status)d %(byte)d',
                'datefmt': '[%Y-%m-%d %H:%M:%S %z]',
                'class': 'logging.Formatter',
            },
        },
    }