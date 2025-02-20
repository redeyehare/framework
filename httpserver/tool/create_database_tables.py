import json
from sqlalchemy import create_engine

import sys
import os


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import T_structure.database_table_structre as dbts
from T_structure.database_table_structre import engine
from T_log.T_log_crud import logger


json_file = "../data/config.json"

with open(json_file, 'r', encoding='utf-8') as file:
    data = json.load(file)


# 打印读取的数据

url =data['database']['sqlite']['test2']
#url="sqlite:///./test.db"


@logger.catch()
def create_tables():

    dbts.Base.metadata.create_all(engine)
create_tables()

#%%



#输出路径,enqueue多进程,enqueue=True 可以支持异步写入，实现多进程安全
#logger.add("file.log", rotation="10 MB", compression="zip",enqueue=True, backtrace=True, diagnose=True)




