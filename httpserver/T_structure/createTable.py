import sys
from pathlib import Path
from sqlalchemy import create_engine

Root_path = Path(__file__).resolve().parent.parent
sys.path.append(str(Root_path))

from T_structure.database_table_structre import Base, user, online_user, test, server_manager
from T_log.T_log_crud import logger
from initial import config_data

# 从全局配置获取数据库URL
url = config_data['database']['sqlite']['test2']
logger.info(f"Using database URL: {url}")

# 创建数据库引擎
engine = create_engine(url, echo=True)

def create_tables():
    """创建所有定义的数据库表"""
    try:
        # 创建所有在Base中定义的表
        Base.metadata.create_all(engine)
        logger.info("Tables created successfully")
    except Exception as e:
        logger.error(f"Error creating tables: {str(e)}")
        raise

if __name__ == "__main__":
    create_tables()