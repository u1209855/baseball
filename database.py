import sqlalchemy
import os
import psycopg2
import models as m
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
Base = declarative_base()


def conn():
    con = psycopg2.connect("host=localhost dbname=baseball user=postgres password = some_password")
    return con


def curs():
    cont = conn()
    c = cont.cursor()
    return cont, c


def sqlalchemy_connect():
    conn_str = 'postgresql+psycopg2://{user}:{password}@localhost:5432/{database}'.\
        format(user="postgres",
               password="some_password",
               database='baseball')
    engine = sqlalchemy.create_engine(conn_str
                                      ,use_batch_mode=True
                                      ,server_side_cursors=True)
    Session = sqlalchemy.orm.sessionmaker(autoflush=False)
    Session.configure(bind=engine)
    session = Session()
    return engine


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


def execute_sql_no_return(sql_location, format_dict=None):
    cons, c = curs()
    with open(sql_location, 'r') as sql_file:
            sql = sql_file.read()

    if format_dict:
        sql = sql.format(**format_dict)
        # print(sql)

    c.execute(sql)
    cons.commit()

