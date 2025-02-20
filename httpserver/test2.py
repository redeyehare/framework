
from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.orm import sessionmaker

# 创建数据库引擎
engine = create_engine('sqlite:///D:/Project/framework/framework/data/test.db', echo=True)

# 创建元数据对象
metadata = MetaData()

users_table = Table('Behavior', metadata, autoload_with=engine)

# 反射表
#metadata.reflect(bind=engine)

# 将元数据保存到文件中
with open('sql/metadata.py', 'w') as f:
    f.write(f"metadata = {metadata.__dict__}\n")
