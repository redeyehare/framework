【mysqld】
#设置MySQL默认端口号
port=3306
#设置mysql的安装目录-你的文件路径
basedir=
#mysql数据库的数据的存放目录
datadir=\data
#允许最大连接数
max_connections=200
#允许连接失败的次数。可防止有人从该主机试图攻击数据库系统
max_connect_errors=10
#服务端使用的字符集默认为UTF8
character-set-server=utf8
#创建新表时将使用的默认存储引擎
 
default-storage-engine=INNODB
#默认使用“mysql_native_password”插件认证
default_authentication_plugin=mysql_native_password
【mysql】
#设置mysql客户端默认字符集
default-character-set=utf8
【client】
#设置mysql客户端连接服务端时默认使用的端口
port=3306
default-character-set=utf8
 
 
 
复制时把【】给删除