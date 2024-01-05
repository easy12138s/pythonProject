# encoding: utf-8
"""
    @version: python3.1
    @author:'EASY'
    @contact: 2418087868@qq.com
    @software: PyCharm
    @file: 建造者模式.py
    @time: 2024/1/5 9:15
"""
# 建造者模式（Builder Pattern）使用多个简单的对象一步一步构建成一个复杂的对象。这种类型的设计模式属于创建型模式，它提供了一种创建对象的最佳方式。
#
# 一个 Builder 类会一步一步构造最终的对象。该 Builder 类是独立于其他对象的。


# 创建产品类
class Computer():
    def __init__(self):
        self.cpu = None
        self.memory = None
        self.hark_disk = None
        self.graphics_card = None

    def set_cpu(self, cpu):
        self.cpu = cpu

    def set_memory(self, memory):
        self.memory = memory

    def set_hard_disk(self, hard_disk):
        self.hark_disk = hard_disk

    def set_graphics_card(self, graphics_card):
        self.graphics_card = graphics_card

    def get_specs(self):
        specs = f'CPU:{self.cpu}\nMemory:{self.memory}\nHard Disk:{self.hark_disk}\nGraphics Card:{self.graphics_card}'
        return specs


# 创建抽象的建造者类
class ComputerBuilder():
    def build_cpu(self):  # 声明构建不同部分的抽象方法
        pass

    def build_memory(self):
        pass

    def build_hard_disk(self):
        pass

    def build_graphics_card(self):
        pass

    def get_computer(self):
        pass


# 创建具体的建造者类
class DesktopBuilder(ComputerBuilder):  # 继承抽象的建造者类
    def __init__(self):
        self.computer = Computer()  # 初始化产品类

    def build_cpu(self):  # 实现抽象建造者方法
        self.computer.set_cpu("Intel Core 7")  # 设置产品类方法值

    def build_memory(self):
        self.computer.set_memory("16GB DDR4")

    def build_hard_disk(self):
        self.computer.set_hard_disk("1TB HDD")

    def build_graphics_card(self):
        self.computer.set_graphics_card("NVIDIA GTX 1050")

    def get_computer(self):
        return self.computer


class LaptopBuilder(ComputerBuilder):
    def __init__(self):
        self.computer = Computer()

    def build_cpu(self):
        self.computer.set_cpu("Intel Core i5")

    def build_memory(self):
        self.computer.set_memory("8GB DDR4")

    def build_hard_disk(self):
        self.computer.set_hard_disk("256GB SSD")

    def build_graphics_card(self):
        self.computer.set_graphics_card("Intergrated")

    def get_computer(self):
        return self.computer


# 创建指挥者
class ComputerAssembler:
    def __init__(self, builder):
        self.builder = builder

    def assemble(self):
        self.builder.build_cpu()  # 调用具体建造者类方法
        self.builder.build_memory()
        self.builder.build_hard_disk()
        self.builder.build_graphics_card()
        return self.builder.get_computer()


# 创建台式计算机
desktop_builder = DesktopBuilder()
desktop_assembler = ComputerAssembler(desktop_builder)
desktop = desktop_assembler.assemble()
print(desktop.get_specs())

# 创建笔记本计算机
laptop_builder = LaptopBuilder()
laptop_assembler = ComputerAssembler(laptop_builder)
laptop = laptop_assembler.assemble()
print(laptop.get_specs())

