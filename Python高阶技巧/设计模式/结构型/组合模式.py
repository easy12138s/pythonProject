# encoding: utf-8
"""
    @version: python3.1
    @author:'EASY'
    @contact: 2418087868@qq.com
    @software: PyCharm
    @file: 组合模式.py
    @time: 2024/1/9 9:41
"""
from abc import abstractmethod, ABC

"""
    组合模式是一种结构型设计模式，它允许将对象组合成树形结构以表示部分-整体的层次结构。通过使用组合模式，客户端可以统一对待单个对象和组合对象。
    
    组件（Component）：定义抽象接口，可以包含子组件的操作。
    叶子（Leaf）：实现组件接口的具体类，表示叶子节点。
    容器（Composite）：实现组件接口的具体类，可以包含子组件。
"""
class Component(ABC):
    @abstractmethod
    def operation(self):
        pass

class Leaf(Component):
    def operation(self):
        return "Leaf"

class Composite(Component):
    def __init__(self):
        self.children = []

    def add(self, component):
        self.children.append(component)

    def remove(self, component):
        self.children.remove(component)

    def operation(self):
        results = []
        for child in self.children:
            results.append(child.operation())
        return f"Branch({', '.join(results)})"