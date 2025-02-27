""" 启动文件 """
from typing import Union

from fastapi import Depends, FastAPI,Request
from fastapi.security import OAuth2PasswordBearer
import uvicorn
from T_manager.routerManager import main_router
from T_manager.T_logCrud import logger
from datetime import datetime

app = FastAPI()

@app.middleware("http")
async def request_monitor(request: Request, call_next):
    try:
        start_time = datetime.now()
        path = request.url.path
        method = request.method
        
        # 记录请求信息
        logger.info(f"收到请求 - 路径: {path}, 方法: {method}")

        # 获取POST请求的数据
        if method == "POST":
            try:
                body = await request.body()
                if body:
                    try:
                        request_data = await request.json()
                        logger.info(f"POST请求数据: {request_data}")
                    except:
                        logger.info(f"POST请求原始数据: {body.decode()}")
            except Exception as e:
                logger.error(f"读取请求数据失败: {str(e)}")

        
        # 执行请求
        response = await call_next(request)
        
        # 记录响应信息
        duration = (datetime.now() - start_time).total_seconds()
        logger.info(f"请求处理完成 - 状态码: {response.status_code}, 耗时: {duration}秒")
        
        return response
    except Exception as e:
        logger.error(f"请求处理异常: {str(e)}")
        raise

# 注册主路由管理器
app.include_router(main_router, tags=["main"])

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)