from models import metadata, db_list
from config import config
import sqlalchemy as sa
from sqlalchemy_utils import database_exists, create_database


def create_db_tables():

    SQL_URL = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8mb4'.format(
        config['MYSQL_USER'], config['MYSQL_PASSWORD'],
        config['MYSQL_HOST'], config['MYSQL_PORT'], config['MYSQL_DB'])

    engine = sa.create_engine(SQL_URL)
    if not database_exists(engine.url):
        create_database(engine.url)
    metadata.drop_all(engine, db_list)
    metadata.create_all(engine, db_list)


if __name__ == '__main__':
    create_db_tables()
