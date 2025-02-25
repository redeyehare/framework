""" 消息路由 """

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from . import messageCrud as crud

user_router = APIRouter()


@user_router.post("/message")
def messageManager(request: UserRequest):
    print(f"收到用户请求: {request.dict()}")
    try:
        match request.key:
            case 'createMail':
                print('创建邮件')

            case 'requestMail':
                print('创建消息')

            case 'deleteMail':
                print('创建消息')

            # 错误
            case _:
                raise HTTPException(status_code=400, detail="无效的操作类型")
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

