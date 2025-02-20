from fastapi import FastAPI, BackgroundTasks
import asyncio
import time
from loguru import logger
import uvicorn
import sys

app = FastAPI()

logger.remove(0)
inf=logger.add(sys.stderr, level="INFO")


@app.get("/")
async def main():
    logger.info("User info in")
    logger.debug("User debug in")
    print("-----")



@app.get("/aa")
async def aa():
    print('******')
    logger.remove(inf)
    logger.add(sys.stderr, level="DEBUG")
    logger.debug("User aa in")
@app.get("/bb")
async def aa():
    print('******')
    logger.remove(0)
    logger.add(sys.stderr, level="INFO")
    logger.debug("User bb in")
# 示例日志输出

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8080)


