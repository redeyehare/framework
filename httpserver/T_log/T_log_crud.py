import json
from pathlib import Path
import sys
import uuid
from datetime import datetime

from loguru import logger
logger.remove()
logger.add(sys.stderr, level="INFO")

Root_path = Path(__file__).resolve().parent.parent
sys.path.append(str(Root_path))
import T_structure.database_table_structre as dbts






@logger.catch()
def insert_log_sqlite():
    session = dbts.Session()
    id =uuid.uuid4().hex
    datatime = datetime.now()
    #datatime=current_datetime.strftime('%Y-%m-%d %H:%M:%S')
    data=dbts.online_user(ID=id,datatime=datatime,host='127.0.0.1',token='123456789')
    session.add(data)
    session.commit()
    session.close()







#日志打印控制
#常规debug打印到本地
def insert_log(log_level):
    logger.remove()
    logger.add(sys.stderr, level=log_level)


