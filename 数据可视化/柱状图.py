from pyecharts.charts import Bar
from pyecharts.options import LabelOpts

# 使用Bar绘制柱状图
bar = Bar()

# 添加x轴
bar.add_xaxis(["中国", "美国", "英国"])
# 添加y轴
bar.add_yaxis("GDP", [30, 20, 10], label_opts=LabelOpts(position="right"))  # 将数据显示在右边

# 反转xy轴
bar.reversal_axis()

# 绘图
bar.render("基础柱状图.html")

