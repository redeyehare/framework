import json
from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.orm import sessionmaker

path1='sqlite:///D:/Project/framework/framework/data/test.db'

path2='sqlite:///E:/project/framework/data/T_database.db'
test='sqlite:///E:/project/framework/httpserver/test.db'


# 创建数据库引擎
engine = create_engine(path2)#, echo=True

# 创建元数据对象
metadata = MetaData()

#users_table = Table('Behavior', metadata, autoload_with=engine)

# 反射表
metadata.reflect(bind=engine)



# 将元数据保存到文件中
#with open('T_database/metadata.py', 'w') as f:
#    f.write(f"metadata = {metadata.__dict__}\n")
print(metadata.tables)

metadata_dict = {}
for table_name, table in metadata.tables.items():
    columns = {}
    for column in table.columns:
        columns[column.name] = str(column.type)  # 获取列名和列类型
    metadata_dict[table_name] = {
        'columns': columns
    }


with open('T_structure/database_metadata.json', 'w', encoding='utf-8') as f:
    json.dump(metadata_dict, f, ensure_ascii=False, indent=4)