
## 基础操作


INSERT 插入
```sql
1
INSERT INTO user(ID,user_name,password)VALUES(12345678,"mahe","1234")
2
INSERT INTO user (1,'Alice')
```

UPDATE 更新
DELETE 删除
SELECT 查询

.open 直接创建空数据库

sqlite3 DatabaseName.db 不会立即创建,需要创建表以后才起作用

.quit 退出数据库



- 存储类型

NULL：表示没有值。

INTEGER：表示整数。SQLite 会根据整数的大小使用不同的字节存储整数（1、2、3、4、6、8 字节）。

REAL：表示浮点数，存储为 8 字节的 IEEE 浮点数。

TEXT：表示文本字符串。SQLite 支持不同的文本编码，包括 UTF-8、UTF-16BE 和 UTF-16LE。在内部，SQLite 通常使用 UTF-8 编码。

BLOB：表示二进制数据。BLOB 类型用于存储二进制大对象，如图片或文件内容。



- 排序规则

BINARY：默认的排序规则，按照字节值进行比较，不考虑任何区域设置。

NOCASE：不区分大小写的比较，将所有字符转换为小写后进行比较。

RTRIM：在比较之前，去掉字符串末尾的空格。







