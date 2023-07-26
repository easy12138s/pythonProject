import json
# 绘制包
from pyecharts.charts import Map
# 标题包
from pyecharts.options import *

# 读取数据文件
with open("D:/河南疫情.txt", "r", encoding="UTF-8") as f:
    data = f.read()

# 转换json数据
data_dict = json.loads(data)

# 获取河南省数据
cities_data = data_dict["areaTree"][0]["children"][3]["children"]


# 遍历出所有城市数据
data_list = []
for city_data in cities_data:
    city_name = city_data["name"] + "市"
    city_confirm = city_data["total"]["confirm"]
    data_list.append((city_name, city_confirm))

# 手动添加济源市
data_list.append(("济源市", 5))

# 构建地图
map = Map()
map.add("各市确诊人数", data_list, "河南")

# 设置全局配置
map.set_global_opts(
    title_opts=TitleOpts(title="河南疫情地图"),
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
map.render("河南疫情地图.html")
