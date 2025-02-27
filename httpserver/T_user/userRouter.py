""" 用户路由 """

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from datetime import datetime
from . import userCrud as crud
from T_manager.T_logCrud import logger
from T_structure.database_structre import user, online_user, Session
from snowflake import SnowflakeGenerator

user_router = APIRouter()

# 创建雪花ID生成器实例
snowflake = SnowflakeGenerator(42)

class UserRequest(BaseModel):
    key: str
    username: str
    password: str = None
    phone: int = None
    email: str = None

@user_router.post("/user")
def create_user(request: UserRequest):
    print(f"收到用户请求: {request.dict()}")
    try:
        match request.key:
            # 登录
            case 'login':
                if not request.phone or not request.password:
                    raise HTTPException(status_code=400, detail="手机号和密码不能为空")
                
                # 业务逻辑：验证用户并创建会话
                session = Session()
                try:
                    # 查询并验证用户
                    user_data = session.query(user).filter_by(phone=request.phone).first()
                    if not user_data:
                        raise HTTPException(status_code=404, detail="用户不存在")
                    if user_data.password != request.password:
                        raise HTTPException(status_code=400, detail="密码错误")
                    
                    # 创建在线用户记录
                    online = online_user(
                        ID=next(snowflake),
                        userID=user_data.ID,
                        datetime=datetime.now(),
                        host="127.0.0.1",
                        token=str(next(snowflake) % 10000000000),
                        offline=0
                    )
                    session.add(online)
                    session.commit()
                    return {"status": "success", "data": {"message": "登录成功", "token": online.token}}
                finally:
                    session.close()
                    
            # 注册
            case 'register':
                if not all([request.username, request.password, request.phone]):
                    raise HTTPException(status_code=400, detail="注册信息不完整")
                
                # 业务逻辑：验证并创建新用户
                session = Session()
                try:
                    # 检查用户是否已存在
                    existing_user = session.query(user).filter_by(phone=request.phone).first()
                    if existing_user:
                        raise HTTPException(status_code=400, detail="该手机号已被注册")
                    
                    # 创建新用户
                    new_user = user(
                        ID=next(snowflake),
                        register_datatime=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                        name=request.username,
                        password=request.password,
                        phone=request.phone,
                        email=request.email,
                        ID_number=12312313,
                        logout=0,
                        blacklist=0,
                        whitelist=0
                    )
                    session.add(new_user)
                    session.commit()
                    return {"status": "success", "data": {"message": "注册成功", "user_id": new_user.ID}}
                finally:
                    session.close()
                    
            # 注销
            case 'logout':
                if not request.username:
                    raise HTTPException(status_code=400, detail="用户名不能为空")
                
                # 业务逻辑：更新用户登录状态
                session = Session()
                try:
                    # 查询用户
                    user_data = session.query(user).filter_by(name=request.username).first()
                    if not user_data:
                        raise HTTPException(status_code=404, detail="用户不存在")
                    
                    # 更新在线用户状态
                    online_data = session.query(online_user).filter_by(userID=user_data.ID, offline=0).first()
                    if online_data:
                        online_data.offline = 1
                        session.commit()
                        return {"status": "success", "data": {"message": "注销成功"}}
                    else:
                        raise HTTPException(status_code=400, detail="用户未登录")
                finally:
                    session.close()
                    
            # 修改
            case 'change':
                if not request.username:
                    raise HTTPException(status_code=400, detail="用户名不能为空")
                
                # 业务逻辑：更新用户信息
                session = Session()
                try:
                    # 查询用户
                    user_data = session.query(user).filter_by(name=request.username).first()
                    if not user_data:
                        raise HTTPException(status_code=404, detail="用户不存在")
                    
                    # 检查是否有需要更新的字段
                    updated = False
                    
                    # 更新用户名
                    if request.username and request.username != user_data.name:
                        user_data.name = request.username
                        updated = True
                    
                    # 更新密码
                    if request.password:
                        if len(request.password) < 4 or len(request.password) > 8:
                            raise HTTPException(status_code=400, detail="密码长度必须在4-8位之间")
                        if request.password == user_data.password:
                            raise HTTPException(status_code=400, detail="新密码不能与原密码相同")
                        user_data.password = request.password
                        updated = True
                    
                    if not updated:
                        raise HTTPException(status_code=400, detail="没有需要更新的信息")
                    
                    session.commit()
                    return {"status": "success", "data": {"message": "用户信息更新成功"}}
                finally:
                    session.close()
                    
            # 错误的key
            case _:
                raise HTTPException(status_code=400, detail="无效的操作类型")
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    





