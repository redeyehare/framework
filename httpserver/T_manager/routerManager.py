""" 主路由管理模块"""

from fastapi import APIRouter, Request, HTTPException
from datetime import datetime
from T_manager.T_logCrud import logger
from T_message import messageCrud
from T_user import userCrud

class MainRouter(APIRouter):
    def __init__(self):
        super().__init__()
        self._init_routes()
        
    def _init_routes(self):
        """初始化路由"""
        from T_user.userRouter import user_router
        from T_api.T_game_router import game_router
        
        # 注册用户路由
        self.include_router(user_router)
        # 注册游戏路由
        self.include_router(game_router)

main_router = MainRouter()