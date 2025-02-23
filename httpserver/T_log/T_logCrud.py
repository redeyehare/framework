""" 日志控制器 """

import json
from pathlib import Path
import sys
import uuid
from datetime import datetime

from loguru import logger
from initial import config_data

# 获取日志路径配置
log_path = Path(config_data['httpserver']['logpath'])
log_path.mkdir(parents=True, exist_ok=True)  # 确保日志目录存在

# 移除默认的日志处理器
logger.remove()

# 添加控制台输出处理器
logger.add(sys.stderr, level="INFO")

# 添加文件输出处理器
log_file = str(log_path / "T_log_{time:YYYY-MM-DD}.txt")
logger.add(
    log_file,
    rotation="00:00",  # 每天零点创建新文件
    retention="30 days",  # 保留30天的日志
    compression=None,
    encoding="utf-8",
    enqueue=True,  # 支持多进程写入
    level="INFO"
)

# 日志打印控制
def insert_log(log_level: str):
    """设置日志级别
    
    Args:
        log_level: 日志级别，如 "DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"
    """
    # 移除所有现有的处理器
    logger.remove()
    
    # 重新添加控制台处理器
    logger.add(sys.stderr, level=log_level)
    
    # 重新添加文件处理器
    logger.add(
        log_file,
        rotation="00:00",
        retention="30 days",
        compression=None,
        encoding="utf-8",
        enqueue=True,
        level=log_level
    )


