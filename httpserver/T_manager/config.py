""" 全局配置引用 """
import json
from pathlib import Path
from T_manager.T_logCrud import logger

config_data = {}

def load_config():
    """加载配置文件到全局变量"""
    try:
        # 修改配置文件路径计算逻辑，指向项目根目录的data文件夹
        config_path = Path(__file__).resolve().parent.parent.parent / 'data' / 'config.json'
        logger.info(f"配置文件路径: {config_path}")
        
        with open(config_path, 'r', encoding='utf-8') as f:
            global config_data
            config_data = json.load(f)
            logger.info("成功加载配置文件")
            
            # 记录主要配置信息
            logger.info(f"数据库配置: {config_data.get('database', {})}")
            logger.info(f"HTTP服务器配置: {config_data.get('httpserver', {})}")
            logger.info(f"游戏服务器配置: {config_data.get('gameserver', {})}")
            
    except Exception as e:
        error_msg = f'加载配置文件失败: {str(e)}'
        logger.error(error_msg)
        raise Exception(error_msg)

# 初始化加载配置
load_config()