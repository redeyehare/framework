""" 游戏路由模块 """

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from datetime import datetime
from T_manager.T_logCrud import logger

game_router = APIRouter()

class GameRequest(BaseModel):
    key: str
    game_id: int = None
    player_id: int = None
    action: str = None

@game_router.post("/game")
def handle_game_request(request: GameRequest):
    """处理游戏相关请求
    
    目前游戏功能尚未实现，返回501状态码
    """
    logger.info(f"收到游戏请求: {request.dict()}")
    raise HTTPException(status_code=501, detail="游戏功能尚未实现")