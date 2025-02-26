""" 整个消息功能模块 """
from sqlalchemy.orm import Session
from ..T_structure.database_structre import mail
from ..initial import get_db
import json
from datetime import datetime
from snowflake import SnowflakeGenerator

#创建公告

#触发公告
def trigger_announcement(_user_id: int, _event_id: int):
    """根据用户ID和事件ID触发公告
    Args:
        user_id (int): 用户ID
        event_id (int): 事件ID
    Returns:
        dict: 公告内容，如果是模板式的则拼接后返回
    """
    _db = next(get_db())
    try:
        # 查询触发表
        trigger_record = _db.query(trigger).filter_by(ID=_event_id).first()
        if not trigger_record:
            raise ValueError("触发事件不存在")
            
        # 检查触发器状态
        if trigger_record.status == 0:
            raise ValueError("触发器已禁用")
            
        # 检查时间有效性
        _current_time = datetime.now()
        if _current_time < trigger_record.start_time:
            raise ValueError("触发器尚未到启用时间")
            
        if _current_time > trigger_record.end_time:
            raise ValueError("触发器已过期")


        # 查询公告表
        announcement_record = _db.query(announcement).filter_by(ID=trigger_record.announcement_id).first()
        if not announcement_record:
            raise ValueError("公告不存在")
        
        # 解析公告内容
        try:
            content = json.loads(announcement_record.content)
        except json.JSONDecodeError:
            raise ValueError("公告内容格式错误")
        
        # 如果存在变量，进行JSON拼装
        if trigger_record.variables:
            try:
                variables = json.loads(trigger_record.variables)
                # 使用模板字符串方式替换变量
                if isinstance(content, str):
                    for key, value in variables.items():
                        content = content.replace(f"{{{key}}}", str(value))
                elif isinstance(content, dict):
                    # 如果content是字典，递归替换所有字符串值中的变量
                    def replace_variables(obj):
                        if isinstance(obj, dict):
                            return {k: replace_variables(v) for k, v in obj.items()}
                        elif isinstance(obj, list):
                            return [replace_variables(item) for item in obj]
                        elif isinstance(obj, str):
                            result = obj
                            for key, value in variables.items():
                                result = result.replace(f"{{{key}}}", str(value))
                            return result
                        return obj
                    content = replace_variables(content)
            except json.JSONDecodeError:
                raise ValueError("变量格式错误")
        
        return {
            "announcement_id": announcement_record.ID,  # 公告ID
            "trigger_id": trigger_record.ID,          # 触发器ID
            "content": content,                      # 公告内容，如果是模板式的则会替换变量
            "target": trigger_record.target,          # 发送目标：大厅/服务器/房间/组队/个人
            "send_time": trigger_record.send_time.isoformat(),  # 发送时间
            "priority": trigger_record.priority,      # 优先级：数字越大优先级越高
            "send_type": trigger_record.send_type    # 发送方式：每天一次/每周一次/每月一次/无限次
        }
    except Exception as e:
        raise Exception(f"触发公告失败: {str(e)}")
    finally:
        _db.close()

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




