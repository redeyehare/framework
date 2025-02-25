import sys
from pathlib import Path
from datetime import datetime
from sqlalchemy.orm import sessionmaker
import json

Root_path = Path(__file__).resolve().parent.parent
sys.path.append(str(Root_path))

from T_structure.database_structre import Base, user, online_user, announcement, trigger, message_read, mail, engine
from T_log.T_logCrud import logger

# 创建会话
Session = sessionmaker(bind=engine)
session = Session()

try:
    # 插入用户数据
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    new_user = user(
        register_datatime=current_time,
        name="测试用户",
        phone=13800138000,
        email="test@example.com",
        ID_number=440101199001011234,
        password="12345678",  # 设置8位数字密码
        logout=0,
        blacklist=0,  # 默认不在黑名单
        whitelist=0  # 默认不在白名单
    )
    session.add(new_user)
    session.flush()  # 刷新会话以获取用户ID
    logger.info(f"创建用户成功，用户ID: {new_user.ID}")

    # 插入在线用户数据
    new_online_user = online_user(
        ID=f"test-{datetime.now().strftime('%Y%m%d%H%M%S')}",  # 使用时间戳生成唯一ID
        userID=new_user.ID,
        datetime=datetime.now(),
        host="127.0.0.1",
        token="test-token-12345",
        offline=0,
    )
    session.add(new_online_user)
    logger.info(f"创建在线用户成功，ID: {new_online_user.ID}")

    # 插入公告数据
    new_announcement = announcement(
        create_time=datetime.now(),
        target="大厅",
        send_type="一次性",
        start_time=datetime.now(),
        end_time=datetime.now().replace(hour=23, minute=59, second=59),
        content=json.dumps({"title": "测试公告", "body": "这是一条测试公告内容"}),
        is_cancelled=0,
        priority=1
    )
    session.add(new_announcement)
    session.flush()
    logger.info(f"创建公告成功，ID: {new_announcement.ID}")

    # 插入触发器数据
    new_trigger = trigger(
        action="test_action",
        status=1,
        create_time=datetime.now()
    )
    session.add(new_trigger)
    session.flush()
    logger.info(f"创建触发器成功，ID: {new_trigger.ID}")

    # 插入已读公告数据
    new_message_read = message_read(
        user_id=new_user.ID,
        message_type="每人一次",
        read_date=datetime.now(),
        read_time=datetime.now(),
        read_count=1,
        announcement_id=new_announcement.ID
    )
    session.add(new_message_read)
    session.flush()
    logger.info(f"创建已读公告记录成功，ID: {new_message_read.ID}")

    # 插入邮件数据
    new_mail = mail(
        user_id=new_user.ID,
        message=json.dumps({"subject": "测试邮件", "content": "这是一封测试邮件内容"})
    )
    session.add(new_mail)
    session.flush()
    logger.info(f"创建邮件成功，ID: {new_mail.ID}")

    # 提交所有更改
    session.commit()
    logger.info("所有测试数据插入成功")

    # 验证数据插入
    users = session.query(user).all()
    online_users = session.query(online_user).all()

    announcements = session.query(announcement).all()
    triggers = session.query(trigger).all()
    message_reads = session.query(message_read).all()
    mails = session.query(mail).all()

    print("\n已插入的数据:")
    print(f"用户数: {len(users)}")
    print(f"在线用户数: {len(online_users)}")

    print(f"公告数: {len(announcements)}")
    print(f"触发器数: {len(triggers)}")
    print(f"已读公告记录数: {len(message_reads)}")
    print(f"邮件数: {len(mails)}")

except Exception as e:
    session.rollback()
    logger.error(f"插入测试数据时发生错误: {str(e)}")
    raise
finally:
    session.close()