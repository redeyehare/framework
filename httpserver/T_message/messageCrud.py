""" 整个消息功能模块 """
from sqlalchemy.orm import Session
from ..T_structure.database_structre import mail
from ..initial import get_db
import json
from datetime import datetime
from snowflake import SnowflakeGenerator

#创建公告

#创建触发公告


#撤销公告


#修改公告
def create_mail(user_id: int, message_content: dict):
    """创建邮件
    Args:
        user_id (int): 用户ID
        message_content (dict): 邮件内容，包含消息体、创建时间等信息
    Returns:
        int: 创建成功的邮件ID
    """


    # 确保message_content包含必要的字段
    if not isinstance(message_content, dict):
        raise ValueError("邮件内容必须是字典格式")
    
    # 添加创建时间、阅读状态和阅读时间字段
    message_content.update({
        "create_datatime": datetime.now().isoformat(),  # 创建时间
        "is_read": False,                              # 是否已读
        "read_time": None                             # 阅读时间，初始为None
    })

    # 将消息内容转换为JSON字符串
    message_json = json.dumps(message_content, ensure_ascii=False)

    # 创建数据库会话
    db = next(get_db())
    try:
        # 创建新邮件记录
        new_mail = mail(
            user_id=user_id,
            message=message_json
        )
        db.add(new_mail)
        db.commit()
        db.refresh(new_mail)
        return new_mail.ID
    except Exception as e:
        db.rollback()
        raise Exception(f"创建邮件失败: {str(e)}")
    finally:
        db.close()
#同步公告
#请求邮件



#维护
#过期删除邮件




