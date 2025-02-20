
from sqlalchemy import create_engine
import sqlalchemy

engine = create_engine('sqlite:///E:/project/framework/data/test.db',echo=True) #E:/project/framework/data/

meta=sqlalchemy.MetaData()


students = sqlalchemy.Table(
    'students',meta,
    sqlalchemy.Column('id',sqlalchemy.Integer,primary_key=True),
    sqlalchemy.Column('first_name',sqlalchemy.String(128)),
    sqlalchemy.Column('last_name',sqlalchemy.String(128))
)
meta.create_all(engine)








"""
with engine.connect() as connection:
    result =connection.execute(users.select())
    for row in result:
        print("````````")
        print(row)
"""
