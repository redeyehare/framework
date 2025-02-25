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

#同步公告

#创建邮件
#邮件内容格式{id,create_datatime,message,is_read,read_time}
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
    
    # 创建新邮件记录
    new_mail = mail(
        user_id=user_id,
        message=""  # 临时空消息，稍后更新
    )
    
    # 创建数据库会话
    db = next(get_db())
    try:
        # 先保存邮件以获取ID
        db.add(new_mail)
        db.flush()
        
        # 添加ID和其他必要字段
        message_content.update({
            "id": new_mail.ID,                          # 邮件ID
            "create_datatime": datetime.now().isoformat(),  # 创建时间
            "is_read": False,                              # 是否已读
            "read_time": None                              # 阅读时间，初始为None
        })
        
        # 将消息内容转换为JSON字符串并更新邮件记录
        message_json = json.dumps(message_content, ensure_ascii=False)
        new_mail.message = message_json

        db.commit()
        return new_mail.ID
    except Exception as e:
        db.rollback()
        raise Exception(f"创建邮件失败: {str(e)}")
    finally:
        db.close()

#请求邮件



#邮件已读
def mark_mail_as_read(mail_id: int):
    """将邮件标记为已读
    Args:
        mail_id (int): 邮件ID
    Returns:
        dict: 更新后的邮件信息
    """
    db = next(get_db())
    try:
        # 查询邮件
        mail_record = db.query(mail).filter_by(ID=mail_id).first()
        if not mail_record:
            raise ValueError("邮件不存在")
        
        # 解析邮件内容
        message_content = json.loads(mail_record.message)
        
        # 更新阅读状态和时间
        message_content["is_read"] = True
        message_content["read_time"] = datetime.now().isoformat()
        
        # 更新邮件内容
        mail_record.message = json.dumps(message_content, ensure_ascii=False)
        
        db.commit()
        return message_content
    except Exception as e:
        db.rollback()
        raise Exception(f"更新邮件状态失败: {str(e)}")
    finally:
        db.close()



#维护
#过期删除邮件




