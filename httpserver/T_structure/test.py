import sys
from pathlib import Path
from datetime import datetime
from sqlalchemy.orm import sessionmaker

Root_path = Path(__file__).resolve().parent.parent
sys.path.append(str(Root_path))

from T_structure.database_table_structre import Base, user, online_user, test, server_manager, engine
from T_log.T_log_crud import logger

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

    # 插入测试表数据
    new_test = test(
        userid=new_user.ID
    )
    session.add(new_test)
    session.flush()
    logger.info(f"创建测试数据成功，ID: {new_test.ID}")

    # 插入服务器管理数据
    new_server = server_manager(
        port=8080
    )
    session.add(new_server)
    session.flush()
    logger.info(f"创建服务器管理数据成功，ID: {new_server.ID}")

    # 提交所有更改
    session.commit()
    logger.info("所有测试数据插入成功")

    # 验证数据插入
    users = session.query(user).all()
    online_users = session.query(online_user).all()
    tests = session.query(test).all()
    servers = session.query(server_manager).all()

    print("\n已插入的数据:")
    print(f"用户数: {len(users)}")
    print(f"在线用户数: {len(online_users)}")
    print(f"测试表记录数: {len(tests)}")
    print(f"服务器管理记录数: {len(servers)}")

except Exception as e:
    session.rollback()
    logger.error(f"插入测试数据时发生错误: {str(e)}")
    raise
finally:
    session.close()