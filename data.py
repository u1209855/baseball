import database as db
import os
baseball_path = os.path.abspath("baseball_files")


def main():
    insert_data()


def join_path(fn):
    return os.path.join(baseball_path, fn)


def insert_data():
    conn = db.conn()
    cur = conn.cursor()
    csv_tables = {'Master.csv': 'master', 'TeamsFranchises.csv': 'team_franchises',
                  'teams.csv': 'teams', 'managers.csv': 'managers',
                  'awardssharemanagers.csv': 'awardssharemanagers',
                  'awardsmanagers.csv': 'awardsmanagers', 'awardsplayers.csv': 'awardsplayers',
                  'awardsshareplayers.csv': 'awardsshareplayers', 'batting.csv': 'batting',
                  'salaries.csv': 'salaries', 'fieldingOF.csv': "fieldingOF",
                  'halloffame.csv': 'halloffame',
                  'seriespost.csv': 'series_post', 'battingpost.csv': 'batting_post',
                  'fielding.csv': 'fielding', 'pitching.csv': 'pitching',
                  'pitchingpost.csv': 'pitching_post', 'allstarfull.csv': 'allstarfull'}
    for i, k in csv_tables.items():

        path = join_path("{i}".format(i=i))
        with open(path, 'r') as f:

            next(f)  # Skip the header row.
            cur.copy_from(f, '{k}'.format(k=k), sep=',', null='')
            conn.commit()
