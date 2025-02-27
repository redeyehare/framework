""" 用户行为 """
from fastapi import HTTPException
from sqlalchemy.orm import Session
from datetime import datetime
import sys
from pathlib import Path

Root_path = Path(__file__).resolve().parent.parent
sys.path.append(str(Root_path))

from T_manager.T_logCrud import logger, snowflake

from T_structure.database_structre import user, online_user, Session

# 登录
@logger.catch()
def login(phone: int, password: str):
    session = Session()
    try:
        # 查询手机号是否存在  
        user_data = session.query(user).filter_by(phone=phone).first()
        if not user_data:
            raise HTTPException(status_code=404, detail="用户不存在")
        # 验证密码
        if user_data.password != password:
            raise HTTPException(status_code=400, detail="密码错误")
        # 检查用户是否已注销
        if user_data.logout == 1:
            raise HTTPException(status_code=400, detail="该账户已注销")
    
        #是否在黑名单
        if user_data.blacklist == 1:
            raise HTTPException(status_code=403, detail="该账户已被列入黑名单")

        # 创建在线用户记录
        online = online_user(
            ID=next(snowflake),  
            userID=user_data.ID,
            datetime=datetime.now(),
            host="127.0.0.1",
            token=str(next(snowflake) % 10000000000),  # 确保生成10位token
            offline=0
        )
        session.add(online)
        session.commit()
        return {"message": "登录成功", "token": online.token}
    except Exception as e:
        logger.error(f"登录过程中发生错误: {str(e)}")
        raise
    finally:
        session.close()

# 注册
@logger.catch()
def register(_username: str, _password: str, _phone: int, _email: str = None,_ID_number: int=None):
    session = Session()
    try:
        # 检查用户是否已存在
        existing_user = session.query(user).filter_by(phone=_phone).first()
        if existing_user:
            raise HTTPException(status_code=400, detail="该手机号已被注册")
        
        # 创建新用户
        new_user = user(
            ID=next(snowflake),  # 使用next()方法生成10位ID
            register_datatime=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            name=_username,
            password=_password,  # 实际应用中应该对密码进行加密
            phone=_phone,
            email=_email,
            ID_number=_ID_number,  # 使用相同的ID作为ID_number
            logout=0,
            blacklist=0,
            whitelist=0
        )
        session.add(new_user)
        session.commit()
        return {"message": "注册成功", "user_id": new_user.ID}
    finally:
        session.close()

# 注销
@logger.catch()
def logout(_ID:int):
    session = Session()
    try:
        # 查询用户
        user_data = session.query(user).filter_by(ID=_ID).first()
        if not user_data:
            raise HTTPException(status_code=404, detail="用户不存在")
        
        # 更新用户注销状态
        user_data.logout = 1
        
        # 更新在线用户状态为离线
        online_data = session.query(online_user).filter_by(userID=_ID, offline=0).first()
        if online_data:
            online_data.offline = 1
        
        session.commit()
        return {"message": "用户注销成功"}
    finally:
        session.close()

# 修改
@logger.catch()
def change(_ID:int,_username: str, _password: str):
    session = Session()
    try:
        # 查询ID
        user_data = session.query(user).filter_by(ID=_ID).first()
        if not user_data:
            raise HTTPException(status_code=404, detail="用户不存在")
        updated = False
        # 更新用户名
        if not _username:
            raise HTTPException(status_code=400, detail="用户名不能为空")
        if len(_username) > 10:
            raise HTTPException(status_code=400, detail="用户名长度不能超过10个字符")
        user_data.name = _username
        updated = True

        # 更新密码
        if _password:
            if len(_password) < 4 or len(_password) > 8:
                raise HTTPException(status_code=400, detail="密码长度必须在4-8位之间")
            if _password == user_data.password:
                raise HTTPException(status_code=400, detail="新密码不能与原密码相同")
            user_data.password = _password
            updated = True

        if not updated:
            raise HTTPException(status_code=400, detail="没有需要更新的信息")
            
        session.commit()
        return {"message": "用户信息更新成功"}
    finally:
        session.close()


#用户离线
@logger.catch()
def offline(_ID:int):
    session = Session()
    try:
        # 查询在线用户记录
        online_data = session.query(online_user).filter_by(userID=_ID, offline=0).first()
        if not online_data:
            raise HTTPException(status_code=404, detail="用户不在线或已离线")
        
        # 更新离线状态
        online_data.offline = 1
        
        session.commit()
        return {"message": "用户已设置为离线状态"}
    finally:
        session.close()



