""" 用户数据库表结构 """
import datetime
import json
import os
from pathlib import Path
import sys
from sqlalchemy import ForeignKey, Integer, String, create_engine, DateTime, event
from sqlalchemy.orm import sessionmaker, Mapped, mapped_column, relationship, declarative_base

# 设置项目根路径
Root_path = Path(__file__).resolve().parent.parent
sys.path.append(str(Root_path))

# 从T_manager.config导入配置
from T_manager.config import config_data

url = config_data['database']['sqlite']['test2']

# 创建数据库引擎
engine = create_engine(url, echo=True)
Base = declarative_base()

#用户表
class user(Base):
    __tablename__='user'
    ID:Mapped[int]=mapped_column(Integer,primary_key=True,index=True)  # 用户ID，主键，索引
    register_datatime:Mapped[str]=mapped_column(String(50),nullable=False)  # 注册日期时间，字符串格式，不能为空
    name:Mapped[str]=mapped_column(String(50))  # 用户姓名
    phone:Mapped[int]=mapped_column(Integer,nullable=False,index=True, unique=True)  # 用户手机号，整数格式，不能为空，索引，唯一
    email:Mapped[str]=mapped_column(String(50))  # 用户邮箱
    ID_number:Mapped[int]=mapped_column(Integer)  # 用户身份证号
    password:Mapped[str]=mapped_column(String(255))  # 密码必须是8位数字
    logout:Mapped[int]=mapped_column(Integer)  # 该字段表示用户的登出状态，0表示未登出，1表示已登出
    # 添加黑白名单字段
    blacklist: Mapped[int] = mapped_column(Integer, default=0)  # 0表示不在黑名单，1表示在黑名单
    # 0表示不在白名单，1表示在白名单
    whitelist: Mapped[int] = mapped_column(Integer, default=0)  
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


""" #日志表
class log(Base):
    __tablename__='log'

#在线房间表
class room(Base):
    __tablename__='room' """








#公告表
class announcement(Base):
    __tablename__ = 'announcement'
    ID: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    create_time: Mapped[DateTime] = mapped_column(DateTime, nullable=False)  # 创建时间
    content: Mapped[str] = mapped_column(String(1000))  # 公告内容，使用JSON字符串存储，格式为{"key1": "value1", "key2": "value2"}




#触发表
class trigger(Base):
    __tablename__ = 'trigger'
    ID: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    create_time: Mapped[DateTime] = mapped_column(DateTime, nullable=False)  # 创建时间
    action: Mapped[str] = mapped_column(String(500), nullable=False)  # 触发动作
    announcement_id: Mapped[int] = mapped_column(Integer, ForeignKey('announcement.ID', ondelete="CASCADE", onupdate="CASCADE"))  # 公告模板ID
    variables: Mapped[str] = mapped_column(String(1000))  # 变量键值对，使用JSON字符串存储
    target: Mapped[str] = mapped_column(String(50), nullable=False)  # 发送目标：大厅/服务器/房间/组队/个人
    start_time: Mapped[DateTime] = mapped_column(DateTime, nullable=False)  # 启用时间
    end_time: Mapped[DateTime] = mapped_column(DateTime, nullable=False)  # 结束时间
    send_time: Mapped[DateTime] = mapped_column(DateTime, nullable=False)  # 发送时间
    send_type: Mapped[str] = mapped_column(String(20), nullable=False)  # 发送方式：每天一次/每周一次/每月一次/无限次
    priority: Mapped[int] = mapped_column(Integer, default=0)  # 优先级：数字越大优先级越高
    is_cancelled: Mapped[int] = mapped_column(Integer, default=0)  # 取消状态：0未取消，1已取消
    status: Mapped[int] = mapped_column(Integer, default=1)  # 触发器状态：1启用，0禁用

    # 添加关系
    announcement = relationship("announcement")

#已读公告表
class message_read(Base):
    __tablename__ = 'message_read'
    ID: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey('user.ID', ondelete="CASCADE", onupdate="CASCADE"))  # 用户ID
    message_type: Mapped[str] = mapped_column(String(20), nullable=False)  # 消息类型：每人一次/每天一次
    read_date: Mapped[DateTime] = mapped_column(DateTime, nullable=False)  # 读取日期
    read_time: Mapped[DateTime] = mapped_column(DateTime, nullable=False)  # 阅读时间
    read_count: Mapped[int] = mapped_column(Integer, default=0)  # 读取次数
    announcement_id: Mapped[int] = mapped_column(Integer, ForeignKey('announcement.ID', ondelete="CASCADE", onupdate="CASCADE"))  # 公告ID

    # 添加关系
    user = relationship("user")
    announcement = relationship("announcement")

#邮件表
class mail(Base):
    __tablename__ = 'mail'
    ID: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey('user.ID', ondelete="CASCADE", onupdate="CASCADE"))  # 用户ID
    message: Mapped[str] = mapped_column(String(1000))  # 邮件内容，使用JSON字符串存储

    # 添加关系
    user = relationship("user")


Session = sessionmaker(bind=engine)