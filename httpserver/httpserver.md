启动程序
检测cpu,内存,主板,数据库

celery


main  业务逻辑
database 配置数据库:名称,地址,创建
models ORM模型操作:有哪些表,表里有哪些属性字段
schemas 响应体数据格式,发送给前端的数据格式
crud 对数据库的crud操作


SQLAlchemy的基本操作大全
http://www.taodudu.cc/news/show-175725.html
Python3+SQLA1chemy+Sqlite3实现ORM教程
https://www.cnblogs.com/jiangxiaobo/p/12350561.html
SQLAlchemy基础知识Autoflush和lAutocommit
https://zhuanlan.zhihu.com/p/48994990



GET /users           # 获取用户列表
GET /users/{id}      # 获取单个用户
POST /users          # 创建新用户
PUT /users/{id}      # 修改用户信息
DELETE /users/{id}   # 删除用户


- 操作
  - login 登录
  - register 注册
  - 认证
  - logout 注销
  - change 修改密码
  - refresh 刷新数据
  - up/down 文件上传,下载

- 返回web页面

- 发送广播

- 返回服务器地址

- 申请大厅数据
- 申请玩家数据
- 申请游戏数据
- 申请比赛数据


