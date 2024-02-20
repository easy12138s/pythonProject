# 导入必要的库
import tkinter  # 导入tkinter库用于GUI
import random  # 导入random库用于生成随机数


class Firework:
    # 初始化烟花对象，包括画布引用、初始坐标、随机颜色以及烟花粒子列表。
    def __init__(self, *args):
        pass

    # 为烟花生成一定数量（99个）的随机速度的粒子，每个粒子用椭圆表示，并存储粒子ID及其速度信息。
    def create_particles(self):
        pass

    # 更新烟花状态，增加粒子半径、减少寿命，并根据粒子速度移动粒子，移除超出画布范围的粒子。
    def update(self):
        pass

    # 在画布上绘制出烟花主体，并启动定时器调用
    def fire(self):
        pass

    # 方法开始连续更新烟花状态。
    def launch(self):
        pass

    # 连续执行
    def launch(self):
        pass

    # 方法，当所有粒子消失或烟花寿命结束时从画布上删除烟花。
    def update(self):
        pass


# 函数：将窗口居中显示
def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x = (screen_width - width) // 2
    y = (screen_height - height) // 2

    window.geometry(f'{width}x{height}+{x}+{y}')  # 设置窗口的位置和大小


# 函数：生成随机颜色
def color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return f'#{r:02x}{g:02x}{b:02x}'  # 返回随机颜色值的字符串表示


# 创建主窗口
root = tkinter.Tk()  # 创建主窗口对象
root.title("新春烟花")  # 设置窗口标题
width = 888
height = 666
center_window(root, width, height)  # 调用center_window函数将窗口居中显示

# 创建画布
canvas = tkinter.Canvas(root, bg='black')  # 创建画布对象，背景色为黑色
canvas.pack(fill=tkinter.BOTH, expand=1)  # 将画布填满整个窗口并扩展


# 鼠标点击事件处理函数
def on_click(event):
    x = event.x
    y = event.y
    firework = Firework(canvas, x, y)  # 创建Firework对象
    firework.fire()  # 发射烟花


# 绑定鼠标点击事件
canvas.bind('<Button-1>', on_click)

# 运行主循环
root.mainloop()  # 启动主循环，等待用户交互事件

