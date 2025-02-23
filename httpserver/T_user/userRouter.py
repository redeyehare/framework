""" 用户路由 """

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from . import userCrud as crud

user_router = APIRouter()

class UserRequest(BaseModel):
    ID : int = None
    key: str
    username: str
    password: str = None
    phone: int = None
    email: str = None
    ID_number: int = None

@user_router.post("/user")
def create_user(request: UserRequest):
    print(f"收到用户请求: {request.dict()}")
    try:
        match request.key:
            # 登录
            case 'login':
                if not request.phone or not request.password:
                    raise HTTPException(status_code=400, detail="手机号和密码不能为空")
                result = crud.login(request.phone, request.password)
                return {"status": "success", "data": result}
            # 注册
            case 'register':
                if not all([request.username, request.password, request.phone]):
                    raise HTTPException(status_code=400, detail="注册信息不完整")
                result = crud.register(request.username, request.password, request.phone, request.email)
                return {"status": "success", "data": result}
            # 注销
            case 'logout':
                if not request.ID:
                    raise HTTPException(status_code=400, detail="用户名不能为空")
                result = crud.logout(request.ID)
                return {"status": "success", "data": result}
            # 修改
            case 'change':
                if not request.ID:
                    raise HTTPException(status_code=400, detail="用户ID不能为空")
                result = crud.change(request.ID,request.username,request.password)

                return {"status": "success", "data": result}
            # 离线
            case 'offline':
                if not request.ID:
                    raise HTTPException(status_code=400, detail="用户ID不能为空")
                result = crud.offline(request.ID)
                return {"status": "success", "data": result}
            # 错误
            case _:
                raise HTTPException(status_code=400, detail="无效的操作类型")
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    





