import datetime
import json
from pathlib import Path
import sys
from sqlalchemy import ForeignKey, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,Mapped,mapped_column
from sqlalchemy import DateTime

Root_path = Path(__file__).resolve().parent.parent
sys.path.append(str(Root_path))
from T_log.T_log_crud import logger


""" path1='sqlite:///D:/Project/framework/framework/data/test.db'

path2='sqlite:///E:/project/framework/data/T_database.db'
test='sqlite:///E:/project/framework/httpserver/test.db' """

json_file = "../data/config.json"

with open(json_file, 'r', encoding='utf-8') as file:
    data = json.load(file)


# 打印读取的数据

url =data['database']['sqlite']['test2']

logger.info(url)

engine = create_engine(url,echo=True)

Base=declarative_base()

class user(Base):
    __tablename__='user'
    ID:Mapped[int]=mapped_column(Integer,primary_key=True)
    register_datatime:Mapped[str]=mapped_column(String(50),nullable=False)
    name:Mapped[str]=mapped_column(String(50))
    phone:Mapped[int]=mapped_column(Integer)
    email:Mapped[str]=mapped_column(String(50))
    ID_number:Mapped[int]=mapped_column(Integer)
    logout:Mapped[int]=mapped_column(Integer)
 
class online_user(Base):
    __tablename__='online_user'
    ID:Mapped[str]=mapped_column(String(36),primary_key=True)
    datetime:Mapped[DateTime]=mapped_column(DateTime)
    host:Mapped[str]=mapped_column(String(40))
    token:Mapped[str]=mapped_column(String(255))
    offline:Mapped[int]=mapped_column(Integer)

Session = sessionmaker(bind=engine)

class test(Base):
    __tablename__='test'
    ID:Mapped[int]=mapped_column(Integer,primary_key=True)
    userid:Mapped[int]=mapped_column(Integer,ForeignKey('user.ID'))


class server_manager(Base):
    __tablename__='server_manager'
    ID:Mapped[int]=mapped_column(Integer,primary_key=True)
    port:Mapped[int]=mapped_column(Integer)


"""




#创建表
Base.metadata.create_all(engine)

Session=sessionmaker(bind=engine)
se = Session()

current_time = datetime.datetime.now()
formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
 """



""" #测试
c=User(ID=11111,name='test',register_datatime=formatted_time,phone=1234567890,email='test@test.com',ID_number='123456789012345678')
#插入数据
se.add(c)    
se.commit()
se.close() """

#
#Session = sessionmaker(bind=engine,autoflush=False,autocommit=False,expire_on_commit=True)
#创建基本的映射类
#Base=declarative_base(bind=engine,name='Base')

""" #%%
class tt(Base):
    id:Mapped[int]=mapped_column(primary_key=True)
    #外键->对应department表的id
    dep id:Mapped[int]=mapped_column(ForeignKey('department.id')))


 """

