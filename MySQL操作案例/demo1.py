from pymysql import connect

# 创建数据库连接对象
conn = connect(
    host="localhost",  # 主机名
    port=3306,
    user="root",
    password="root",
    autocommit=True     # 自动提交
)
cursor = conn.cursor()  # 获取游标对象
conn.select_db("pydatebase")  # 选择数据库

cursor.execute("insert into test values(1)")

# commit提交 ,autocommit=True 设置后就不用再手动commit
# conn.commit()

cursor.execute("select * from orders")

results: tuple = cursor.fetchall()

for l in results:
    print(l)

# 关闭数据库连接
conn.close()
