from sanic.config import Config

# from . import base as base_config
from .log import get_log_config

# config = Config(load_env=False)
#
# config.from_object(base_config)
# config.load_environment_vars('LI_')

import os


def load_config():
    """
    Load a config class
    """
    mode = os.environ.get('MODE', 'LOC')
    print("environ mode", mode)
    try:
        if mode == 'PRO':
            from .product_config import ProductConfig
            return ProductConfig
        elif mode == 'LOC':
            from .local_config import LocalConfig
            return LocalConfig
        else:
            from .local_config import LocalConfig
            return LocalConfig
    except ImportError:
        from .config import Config
        return Config


CONFIG = load_config()

log_config = get_log_config(CONFIG)
