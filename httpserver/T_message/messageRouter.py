""" 消息路由 """

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from . import messageCrud as crud

user_router = APIRouter()

class UserRequest(BaseModel):
    key: str
    user_id: int = None
    message_content: dict = None


@user_router.post("/message")
def messageManager(request: UserRequest):
    print(f"收到用户请求: {request.dict()}")
    try:
        match request.key:
            case 'createMail':
                if not request.user_id:
                    raise HTTPException(status_code=400, detail="用户ID不能为空")
                if not request.message_content:
                    raise HTTPException(status_code=400, detail="邮件内容不能为空")
                
                result = crud.create_mail(request.user_id, request.message_content)
                return {"status": "success", "data": {"mail_id": result}}

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

