""" 启动文件 """
from typing import Union

from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordBearer
import uvicorn
from api_router import router
from T_user.userRouter import user_router
from T_log.T_log_crud import logger


app = FastAPI()



# app.include_router(router,tags=["user"])
app.include_router(user_router,tags=["user"])

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


oauth2_schema=OAuth2PasswordBearer(tokenUrl="/token")

@app.get("/oauth2_password_bearer")
async def oauth2_password_bearer(token: str = Depends(oauth2_schema)):
    return{"token":token}


fake_users_db = {
    "johndoe": {
        "username": "johndoe",
        "full_name": "John Doe",
        "email": "johndoe@example.com",
        "hashed_password": "$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW",
        "disabled": False,
    }
}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)