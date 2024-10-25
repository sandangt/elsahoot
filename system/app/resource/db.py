from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from settings import POSTGRES

__db_engine = create_engine(
    'postgresql+psycopg://{username}:{password}@{host}:{port}/{db_name}'.format(
        username=POSTGRES['user'],
        password=POSTGRES['password'],
        host=POSTGRES['host'],
        port=POSTGRES['port'],
        db_name=POSTGRES['db'],
    )
)

db_session = sessionmaker(bind=__db_engine, autoflush=False, autocommit=False)
