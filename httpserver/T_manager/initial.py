""" 初始化 """

import json
import sys
from pathlib import Path
from T_manager.T_logCrud import logger
from sqlalchemy.orm import sessionmaker
from T_structure.database_structre import engine

logger.remove()
logger.add(sys.stderr, level="INFO")



# 创建Session工厂
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    """获取数据库会话
    Yields:
        Session: 数据库会话对象
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


