import sys

sys.path.append('.')
from config.config import Config
import logging


# ====================
# dev environment config
# ===============================

class ProductConfig(Config):
    DEBUG = True
    HOST = '0.0.0.0'
    PORT = 15236
    ACCESS_LOG = True
    AUTO_RELOAD = True
    WORKERS = 1
    # 常规配置，默认
    REQUEST_MAX_SIZE = 100000000
    REQUEST_BUFFER_QUEUE_SIZE = 100
    REQUEST_TIMEOUT = 60
    RESPONSE_TIMEOUT = 60
    KEEP_ALIVE = True
    KEEP_ALIVE_TIMEOUT = 5
    GRACEFUL_SHUTDOWN_TIMEOUT = 15.0
    DATA_PATH = 'log'

    NAME = 'CC-EBAY'
    LOGO = """
            CC-EBAY
            qiant.ai cc-ebay
            """

    SESSION_EXPIRY = 30 * 24 * 3600

    MYSQL_HOST = '127.0.0.1'
    MYSQL_PORT = 3306
    MYSQL_DB = 'saas_cc_dev'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = '123'
    MYSQL_TIMEOUT = 1
    MYSQL_POOL_MIN_SIZE = 1
    MYSQL_POOL_MAX_SIZE = 100

    # Redis connection parameters
    REDIS_URI = 'redis://@127.0.0.1:30020/1'
    REDIS_TIMEOUT = 1
    REDIS_POOL_MIN_SIZE = 1
    REDIS_POOL_MAX_SIZE = 100
    USER_TOKEN_EXPIRE = 24 * 3600

    NACOS_SERVER_ADDRESSES = "127.0.0.1:8848"
    NACOS_NAMESPACE = "public"

    NACOS_APPLICATION_NAME = "cc-ebay"
    NACOS_IP = "127.0.0.1"