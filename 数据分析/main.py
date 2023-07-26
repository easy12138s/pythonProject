"""
    数据分析案例主文件
"""
from file_define import FileReader, TextFileReader, JsonFileReader
from date_define import Record
from pyecharts.charts import Bar
from pyecharts.options import *
from pyecharts.globals import ThemeType

# 定义获取两种类型数据对象
text_file_reader = TextFileReader("E:/pythonProject/数据分析/2011年1月销售数据.txt")
json_file_reader = JsonFileReader("E:/pythonProject/数据分析/2011年2月销售数据JSON.txt")

jan_date: list[Record] = text_file_reader.read_date()
feb_date: list[Record] = json_file_reader.read_date()
# 将两个月的list合并为一个
all_list: list[Record] = jan_date + feb_date

# 计算数据,计算每一天的销售额
# {"2011-01-01": 1234}
data_dict = {}
for record in all_list:
    if record.date in data_dict.keys():
        # 表明字典有当前日期数据，和老记录做累加即可
        data_dict[record.date] += record.money
    else:
        # 表明没有当前日期数据，添加当前日期key和金额
        data_dict[record.date] = record.money

# 可视化部分
bar = Bar(init_opts=InitOpts(theme=ThemeType.LIGHT))
bar.add_xaxis(list(data_dict.keys()))
bar.add_yaxis("销售额", list(data_dict.values()), label_opts=LabelOpts(is_show=False))  # 添加y轴数据，并且设置数值不可见

bar.set_global_opts(
    title_opts=TitleOpts("每日销售额")
)

bar.render("每日销售额柱状图.html")
