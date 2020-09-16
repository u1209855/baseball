import database as db
import os

sql_path = os.path.abspath("sql_files")


def main():
    create_warehouse()


def join_path(fn):
    return os.path.join(sql_path, fn)


def create_warehouse():
    # print("Creating schema")
    # db.execute_sql_no_return(join_path('create_schema.sql'))
    files = ['master.sql', 'teamfranchises.sql']

    for i in files:
        print("Creating {x} master and deleting stg {x}".format(x=i))
        db.execute_sql_no_return(join_path('{x}'.format(x=i)))