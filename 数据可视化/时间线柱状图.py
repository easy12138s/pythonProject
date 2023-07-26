from pyecharts.charts import Bar, Timeline
from pyecharts.options import LabelOpts
from pyecharts.globals import ThemeType

# 时间线每一个时间点其实就是一个柱状图
bar1 = Bar()
bar1.add_xaxis(["中国", "美国", "英国"])
bar1.add_yaxis("GDP", [30, 20, 10], label_opts=LabelOpts(position="right"))  # 将数据显示在右边
bar1.reversal_axis()

bar2 = Bar()
bar2.add_xaxis(["中国", "美国", "英国"])
bar2.add_yaxis("GDP", [50, 40, 20], label_opts=LabelOpts(position="right"))  # 将数据显示在右边
bar2.reversal_axis()

bar3 = Bar()
bar3.add_xaxis(["中国", "美国", "英国"])
bar3.add_yaxis("GDP", [70, 50, 30], label_opts=LabelOpts(position="right"))  # 将数据显示在右边
bar3.reversal_axis()

# 构建时间线对象
timeline = Timeline(
    {"theme": ThemeType.LIGHT}
)
# 在时间线添加柱状图对象
timeline.add(bar1, "点1")
timeline.add(bar2, "点2")
timeline.add(bar3, "点3")
# 自动播放设置
timeline.add_schema(
    play_interval=1000,     # 自动播放时间间隔
    is_timeline_show=True,  # 是否显示时间线
    is_auto_play=True,      # 是否自动播放
    is_loop_play=True       # 是否循环自动播放
)
# 绘图用时间线对象，不是用bar
timeline.render("时间线柱状图.html")
