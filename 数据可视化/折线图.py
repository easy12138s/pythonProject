# 绘制包
from pyecharts.charts import Line
# 标题等包
from pyecharts.options import TitleOpts, LegendOpts


# 得到折线图对象
line = Line()
# 添加x轴数据
line.add_xaxis(["中国", "美国", "英国"])
# 添加y轴数据
line.add_yaxis("GDP", [30, 20, 10])
# 设置全局配置
line.set_global_opts(
    title_opts=TitleOpts(title="GDP展示", pos_left="center", pos_bottom="1%")

)


# 生成图表
line.render()

