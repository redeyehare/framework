""" 用户数据库表结构 """
import datetime
import json
from pathlib import Path
import sys
from sqlalchemy import ForeignKey, Integer, String, create_engine

from sqlalchemy.orm import sessionmaker,Mapped,mapped_column,relationship,declarative_base
from sqlalchemy import DateTime,event

Root_path = Path(__file__).resolve().parent.parent
sys.path.append(str(Root_path))
from T_log.T_logCrud import logger
from initial import config_data


# 打印读取的数据

url =config_data['database']['sqlite']['test2']

logger.info(url)

engine = create_engine(url,echo=True)

Base=declarative_base()

#用户表
class user(Base):
    __tablename__='user'
    ID:Mapped[int]=mapped_column(Integer,primary_key=True,index=True)
    register_datatime:Mapped[str]=mapped_column(String(50),nullable=False)
    name:Mapped[str]=mapped_column(String(50))
    phone:Mapped[int]=mapped_column(Integer,nullable=False,index=True)
    email:Mapped[str]=mapped_column(String(50))
    ID_number:Mapped[int]=mapped_column(Integer)
    password:Mapped[str]=mapped_column(String(255))  # 密码必须是8位数字
    logout:Mapped[int]=mapped_column(Integer)
    # 添加黑白名单字段
    blacklist: Mapped[int] = mapped_column(Integer, default=0)  
    # 0表示不在黑名单，1表示在黑名单
    whitelist: Mapped[int] = mapped_column(Integer, default=0)  
    # 0表示不在白名单，1表示在白名单
    # 添加关系
    online_users = relationship("online_user", back_populates="user")

#在线用户表
class online_user(Base):
    __tablename__='online_user'
    ID:Mapped[str]=mapped_column(String(36),primary_key=True)
    userID:Mapped[int]=mapped_column(Integer,ForeignKey('user.ID', ondelete="CASCADE", onupdate="CASCADE"))
    datetime:Mapped[DateTime]=mapped_column(DateTime)
    host:Mapped[str]=mapped_column(String(40))
    token:Mapped[str]=mapped_column(String(255))
    offline:Mapped[int]=mapped_column(Integer)

    # 添加关系
    user = relationship("user", back_populates="online_users")


#日志表
class log(Base):
    __tablename__='log'

#在线房间表
class room(Base):
    __tablename__='room'


Session = sessionmaker(bind=engine)







#测试
class test(Base):
    __tablename__='test'
    ID:Mapped[int]=mapped_column(Integer,primary_key=True)
    userid:Mapped[int]=mapped_column(Integer,ForeignKey('user.ID'))


class server_manager(Base):
    __tablename__='server_manager'
    ID:Mapped[int]=mapped_column(Integer,primary_key=True)
    port:Mapped[int]=mapped_column(Integer)


