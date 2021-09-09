NAME = 'fund_service'

DATA_PATH = 'log'
HOST = '0.0.0.0'
PORT = 15236

DEBUG = True

# 热加载
AUTO_RELOAD = False
# 访问记录
ACCESS_LOG = True
WORKERS = 1

SESSION_EXPIRY = 30 * 24 * 3600

# MySQL connection parameters
MYSQL_HOST = 'localhost'
MYSQL_PORT = 3309
MYSQL_DB = 'fund_db'
MYSQL_USER = 'root'
MYSQL_PASSWORD = '123'
MYSQL_TIMEOUT = 1
MYSQL_POOL_MIN_SIZE = 1
MYSQL_POOL_MAX_SIZE = 100

# Redis connection parameters
REDIS_URI = 'redis://@localhost:6379/1'
REDIS_TIMEOUT = 1
REDIS_POOL_MIN_SIZE = 1
REDIS_POOL_MAX_SIZE = 100
USER_TOKEN_EXPIRE = 24 * 3600