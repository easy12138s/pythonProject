# 绘制包
from pyecharts.charts import Map
# 标题包
from pyecharts.options import *

import json

# 读取数据文件
with open("D:/疫情数据.txt", "r", encoding="UTF-8") as f:
    data = f.read()
# 将json数据转换为字典
data_dict = json.loads(data)
# 过滤出各省份数据
province_data_list = data_dict["areaTree"][0]["children"]
# 组装每个省份的元素为元组，并将数据封装入列表
data_list = []          # 绘图需要的数据列表
for province_data in province_data_list:
    province_name = province_data["name"]                   # 省份名称
    province_confirm = province_data["total"]["confirm"]    # 确诊人数
    data_list.append((province_name, province_confirm))

# 绘制地图 ,添加数据
map = Map()
map.add("各省确诊人数", data_list, "china")

# 设置全局配置
map.set_global_opts(
    title_opts=TitleOpts(title="全国疫情地图"),
    visualmap_opts=VisualMapOpts(
        is_show=True,           # 是否显示
        is_piecewise=True,      # 是否分段
        pieces=[
            {"min": 1, "max": 99, "lable": "1~99", "color": "#CCFFFF"},
            {"min": 100, "max": 999, "lable": "100~999", "color": "#FFFF99"},
            {"min": 1000, "max": 4999, "lable": "1000~4999", "color": "#FF9966"},
            {"min": 5000, "max": 9999, "lable": "5000~9999", "color": "#FF6666"},
            {"min": 10000, "max": 99999, "lable": "10000~99999", "color": "#CC3333"},
            {"min": 100000,  "lable": "100000+", "color": "#990033"},
        ]
    )
)

# 绘图
map.render("全国疫情地图.html")
