from fastapi import FastAPI
from sqlalchemy import Column, create_engine,String,Integer, inspect
import uvicorn

from sqlalchemy.orm import sessionmaker,declarative_base

engine = create_engine('sqlite+pysqlite:///:memory:', echo=True)
Base = declarative_base()
conn = engine.connect()
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

    # 创建一个User对象并插入数据
user = User(name='Alice', age=25)
session.add(user)

    # 提交事务
session.commit()
session.flush()

inspector = inspect(engine)
table_names = inspector.get_table_names()
for table_name in table_names:
    print(table_name)
users = session.query(User).all()
print(users)

app = FastAPI()


    

    

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8080)
    print('1111')