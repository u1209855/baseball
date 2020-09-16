import database as db
import os
baseball_path = os.path.abspath("baseball_files")


def main():
    insert_master()


def join_path(fn):
    return os.path.join(baseball_path, fn)


def insert_master():
    conn = db.conn()
    cur = conn.cursor()
    master_csv_path = join_path("Master.csv")
    with open(master_csv_path, 'r') as f:
        # Notice that we don't need the `csv` module.
        next(f)  # Skip the header row.
        cur.copy_from(f, 'master', sep=',', null='')

    conn.commit()
