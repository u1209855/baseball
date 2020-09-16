import models as m
import database as db
import data
import create_warehouse as cw

if __name__ == '__main__':
    engine, session = db.sqlalchemy_session()
    m.create_models(engine)
    data.main()
    cw.main()
