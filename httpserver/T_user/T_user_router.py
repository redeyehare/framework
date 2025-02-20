from fastapi import APIRouter
import T_user_crud as crud

user_router=APIRouter()

@user_router.post("/user")
def create_user(key: str):
    match key:
        # 登录
        case 'login':
            crud.login()
            return "login";
        # 注册
        case 'register':
            return "register";
        #注销
        case 'logout':
            return "logout";
        #修改
        case 'change':
            return "change";
        #错误
        case _:
            return "error";
    





