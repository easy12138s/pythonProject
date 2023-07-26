from pyecharts.charts import Bar, Timeline
from pyecharts.options import LabelOpts, TitleOpts
from pyecharts.globals import ThemeType

# #  准备列表,sort排序测试
# my_list = [["a", 11], ["b", 22], ["c", 55]]
#
# 1、排序函数，使用下标 1 作为排序key
# def choose_sort_key(element):
#     return element[1]
#
# my_list.sort(key=choose_sort_key, reverse=True)
#
# 2、匿名函数进行排序
# my_list.sort(key=lambda element: element[1], reverse=True)
# print(my_list)

# 创建数据文件对象
with open("D：/1960-2019全球GDP数据.csv", "r", "GB2312") as f:
    data_lines = f.readlines()

# 删除第一行无用数据
data_lines.pop(0)

# 处理源数据为字典
# {1960: [[美国, 123], [中国, 456].......], 1961: [[美国, 123], [中国, 456].......], ....... }
data_dict = {}
for line in data_lines:
    year = int(line.split(",")[0])      # 年份
    country = line.split(",")[1]        # 国家
    gdp = float(line.split(",")[2])     # GDP
    # 判断字典里有没有已经存在指定的key,没有指定的key会报KeyError异常 有了就不会
    # 利用异常机制，有就直接添加value 没有就先添加key
    try:
        data_dict[year].append([country, gdp])
    except KeyError:
        data_dict[year] = []
        data_dict[year].append([country, gdp])

# 每一个时间线的点都是一个柱状图
# 创建时间线对象
time_line = Timeline({"theme": ThemeType.LIGHT})

# 排序年份,然后只取前八的国家
sorted_year_list = sorted(data_dict.keys())
for year in sorted_year_list:
    data_dict[year].sort(key=lambda element: element[1], reverse=True)  # 排序列表
    year_data = data_dict[year][0:8]
    x_data = []
    y_data = []
    for country_gdp in year_data:
        x_data.append(country_gdp[0])  # 添加国家
        y_data.append(country_gdp[1] / 100000000)   # 添加数值

    # 构建柱状图
    bar = Bar()
    x_data.reverse()
    y_data.reverse()
    bar.add_xaxis(x_data)
    bar.add_yaxis("GDP(亿元)", y_data, label_opts=LabelOpts(position="right"))  # 数值显示在柱状图右边
    # 反转xy轴
    bar.reversal_axis()
    # 设置每一年的图标的标题
    bar.set_global_opts(
        title_opts=TitleOpts(title=f"{year}年全球前8GDP数据")
    )
    time_line.add(bar, str(year))

# 设置自动播放
time_line.add_schema(
    play_interval=1000,
    is_timeline_show=True,
    is_auto_play=True,
    is_loop_play=False
)
# 绘图
time_line.render("1960-2019全球前八GDP数据.html")
