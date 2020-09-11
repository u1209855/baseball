import sqlalchemy
import os
import models as m
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
import psycopg2
from urllib.parse import quote_plus


def sqlalchemy_connect():
    conn_str = 'postgresql+psycopg2://{user}:{password}@localhost:5432/{database}'.\
        format(user="postgres",
               password="some_password",
               database='postgres')
    engine = sqlalchemy.create_engine(conn_str
                                      ,use_batch_mode=True
                                      ,server_side_cursors=True)
    Session = sqlalchemy.orm.sessionmaker(autoflush=False)
    Session.configure(bind=engine)
    session = Session()
    return engine, session


def sqlalchemy_session():
    engine = sqlalchemy_connect()
    session = sqlalchemy.orm.scoped_session(sqlalchemy.orm.sessionmaker())
    session.configure(bind=engine, autoflush=False, expire_on_commit=False)
    return engine, session


def main():
    engine = sqlalchemy_connect()
    m.create_models(engine)


def sqlalchemy_execute_raw(engine, sql):
    with engine.connect() as conn:
        result = conn.execute(sql)
        columns = result.keys()
        result_generator = [dict(zip(columns, row)) for row in result.fetchall()]

        return result_generator


def sqlalchemy_execute_sql_file(engine, sql_file):
    path = os.path.join(os.path.abspath('./sql/'), sql_file)
    with open(path, 'r') as readfile:
        return sqlalchemy_execute_raw(engine, readfile.read())


def sqlalchemy_execute_raw_noret(session, sql):
    session.commit()
    session.execute(sql)
    session.commit()


def sqlalchemy_engine_raw_noret(engine, sql):
    with engine.connect() as conn:
        conn.execute(sql)


def sqlalchemy_execute_sql_file_noret(session, sql_file):
    path = os.path.join(os.path.abspath('./sql'), sql_file)
    with open(path, 'r') as readfile:
        sqlalchemy_execute_raw_noret(session, readfile.read())
