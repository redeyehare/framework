import json
import time
 
from fastapi import FastAPI, Query, Path
import uvicorn
from starlette.requests import Request
import asyncio
from sse_starlette import EventSourceResponse
 
app = FastAPI()
 
 
@app.get("/stream")
async def flush_stream(request: Request):
    async def event_generator(request: Request):
        res_str = "这是一个流式输出他会将每个字挨个挨个的输出哈哈！！！"
        for idx, word in enumerate(res_str):
            if await request.is_disconnected():
                print("连接已中断")
                break
            data = json.dumps({"id": idx, "message": word}, ensure_ascii=False)
            yield data
            await asyncio.sleep(1)
 
    return EventSourceResponse(event_generator(request))
 
 
if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8080)