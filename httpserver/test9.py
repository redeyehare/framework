
from datetime import datetime
import uuid


id =uuid.uuid4().hex
id2=str(uuid.uuid4())

print(id)
print(id2)


current_datetime = datetime.now()
print(current_datetime)

formatted_datetime = current_datetime.strftime('%Y-%m-%d %H:%M:%S')
print(f'格式化后的当前日期和时间: {formatted_datetime}')




import sys
from loguru import logger

#logger.remove()
ll=logger.add(sys.stderr, level="INFO")
logger.info("User bb in")

