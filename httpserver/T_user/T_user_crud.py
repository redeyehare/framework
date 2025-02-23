""" 用户行为 """

import uuid
from datetime import datetime
from pathlib import Path
import sys

from sqlalchemy import update



Root_path = Path(__file__).resolve().parent.parent
sys.path.append(str(Root_path))
import T_structure.database_table_structre as dbts
from T_log.T_log_crud import logger



#user操作


#查询user表是否有相同手机号


#查询user手机号,密码


#插入user表数据

#修改密码



#user_online操作
#插入user_onlie数据
@logger.catch()
def insert_log_sqlite():
    session = dbts.Session()
    id =uuid.uuid4().hex
    _current_datetime = datetime.now()
    print(_current_datetime)

    #datetime_object = datetime.strptime(_current_datetime,'%Y-%m-%d %H:%M:%S')
    _date=dbts.online_user(ID=id,datetime=_current_datetime,host='127.0.0.1',token='123456789')
    session.add(_date)
    session.commit()
    session.close()

#insert_log_sqlite()




#查询user_online表数据,查询是否出一离线状态
@logger.catch()
def get__log_sqlite():
    user_id='1112'
    session = dbts.Session()
    user_result = session.query(dbts.online_user).filter_by(ID=user_id).first()
    if user_result is not None:
        logger.info(user_result)
    else:
        logger.info("user not found")
    session.commit()
    session.close()
    
#get__log_sqlite()

#修改user_online激活在线状态
@logger.catch()
def change__log_sqlite():
    session = dbts.Session()
    try:
    # 开始一个新的事务
        with session.begin():
        # 执行一些数据库操作
            # 创建更新查询
            stmt = (
                update(dbts.online_user)  # 指定要更新的表
                .where(dbts.online_user.ID == '111')  # 指定要更新的记录
                .values(offline='1')  # 新的 token 值
            )
            session.execute(stmt)
        # 如果一切顺利，提交事务
            session.commit()
    except Exception as e:
    # 如果发生异常，回滚事务
        session.rollback()
        raise
    finally:
    # 关闭Session
        session.close()

#change__log_sqlite()
#删除--每天12点清理一次离线状态的数据

@logger.catch()
def test():
    session = dbts.Session()
    with session.begin():
        data=dbts.test(ID='222',userid='111')
        session.add(data)
        session.commit()
        session.close()
        session.flush()
#test()


@logger.catch()
def get_test():
    session = dbts.Session()
    user_result = session.query(dbts.test).filter_by(ID='111').first()
    logger.info(user_result.__dict__.items())

    session.commit()
#get_test()