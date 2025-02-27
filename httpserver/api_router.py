import json
import time
from fastapi import APIRouter
from datetime import datetime
from T_manager.T_logCrud import logger

router = APIRouter()


#登录--验证手机号,密码,
@router.post('/user/{message}')
def login(message: str):
    data=json.loads(message)
    current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    Ordertime=int(time.time())
    return {'message': data,"datetime": current_datetime,"Ordertime":Ordertime}

#注册--手机号密码
@router.get('/user/{message}')
def logout(message: str):
    print()

#修改密码--手机号查询并修改
@router.put('/user/{message}')
def logout(message: str):
    print()

#游客登录-->用户id为1
@router.post('/guest/{message}')
def login(message: str):
    pass


#token验证
@router.post('/token/{message}')
def login(message: str):
    pass
