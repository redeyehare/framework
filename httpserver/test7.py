import structlog
import traceback
from loguru import logger
# 创建 StructLog 实例
loggeu = structlog.get_logger()

# 结构化日志记录
loggeu.info("User logged in", user_id=123, username="john_doe")
try:
    y=1/0
except Exception as e:
# 异常处理并记录日志
    #loggeu.error("An error occurred", exc_info=True)
    #loggeu.error(traceback.format_exc())
    logger.exception(e)
    
