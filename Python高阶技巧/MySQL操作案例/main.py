"""
    数据分析案例主文件
"""
from file_define import FileReader, TextFileReader, JsonFileReader
from date_define import Record
from pyecharts.charts import Bar
from pyecharts.options import *
from pyecharts.globals import ThemeType
from pymysql import connect

# 定义获取两种类型数据对象
text_file_reader = TextFileReader("E:/pythonProject/MySQL操作案例/2011年1月销售数据.txt")
json_file_reader = JsonFileReader("E:/pythonProject/MySQL操作案例/2011年2月销售数据JSON.txt")

jan_date: list[Record] = text_file_reader.read_date()
feb_date: list[Record] = json_file_reader.read_date()
# 将两个月的list合并为一个
all_list: list[Record] = jan_date + feb_date

# 创建数据库连接对象
conn = connect(
    host="localhost",  # 主机名
    port=3306,
    user="root",
    password="root",
    autocommit=True     # 自动提交
)
# 获取游标对象
cursor = conn.cursor()
# 选择数据库
conn.select_db("pydatebase")

for record in all_list:
    sql = f"insert into orders(order_date, order_id, money, province) " \
          f"values('{record.date}', '{record.order_id}', '{record.money}', '{record.province}')"

    cursor.execute(sql)

conn.close()
