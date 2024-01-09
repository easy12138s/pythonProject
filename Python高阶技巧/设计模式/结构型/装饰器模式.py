# encoding: utf-8
"""
    @version: python3.1
    @author:'EASY'
    @contact: 2418087868@qq.com
    @software: PyCharm
    @file: 装饰器模式.py
    @time: 2024/1/9 9:46
"""
from abc import abstractmethod, ABC

"""
    装饰器模式是一种结构型设计模式，它允许向对象动态添加新功能，通过将对象包装在一个装饰器类的实例中，这个装饰器类可以添加额外的行为而不改变原始类的结构。

    组件（Component）：定义一个接口，为具体组件和装饰器提供一致的接口。
    具体组件（Concrete Component）：实现组件接口，是被装饰的对象。
    装饰器（Decorator）：继承或实现组件接口，并包含一个对组件的引用，用于动态地添加新的行为。
    具体装饰器（Concrete Decorator）：扩展装饰器类，实现新的行为。
"""
class Component(ABC):
    @abstractmethod
    def operation(self):
        pass

class ConcreteComponent(Component):
    def operation(self):
        return "ConcreteComponent"

class Decorator(Component):
    def __init__(self, component):
        self._component = component

    def operation(self):
        return f"Decorator({self._component.operation()})"

class ConcreteDecoratorA(Decorator):
    def operation(self):
        return f"ConcreteDecoratorA({self._component.operation()})"