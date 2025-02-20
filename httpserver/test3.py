from fastapi import FastAPI, BackgroundTasks
import asyncio
import time

import uvicorn

app = FastAPI()

def start_background_task(background_tasks: BackgroundTasks):
    def background_task():
        while True:
            print("Background task is running...")
            time.sleep(1)  # 休眠1秒，避免过度占用CPU
        print("Background task has been cancelled.")
        
    background_tasks.add_task(background_task)

@app.get("/")
async def main(background_tasks: BackgroundTasks):
    start_background_task(background_tasks)
    return {"message": "Hello World"}

uvicorn.run(app, host="127.0.0.1", port=8000)