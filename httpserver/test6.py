import sys
from time import sleep
from loguru import logger

while True:
    user_input = input("请输入 yes 或 no: ")
    if user_input == 'yes':
        print("您输入的是 yes")
    elif user_input == 'no':
        print("您输入的是 no")
    else:
        print("无效输入，请重新输入")
    sleep(3)


        