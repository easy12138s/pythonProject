# encoding: utf-8
"""
    @version: python3.1
    @author:'EASY'
    @contact: 2418087868@qq.com
    @software: PyCharm
    @file: 桥接模式.py
    @time: 2024/1/9 9:33
"""
"""
     桥接模式是一种结构型设计模式，它将一个抽象部分与其实现部分分离，使它们可以独立地变化。
     这种模式通过将继承关系转化为组合关系，从而降低了抽象和实现两个层次的耦合度。
     
     抽象类（Abstraction）：定义抽象部分的接口，并维护一个指向实现部分的引用。
     扩充抽象类（Refined Abstraction）：扩展抽象部分的接口。
     实现类接口（Implementor）：定义实现部分的接口，供抽象类调用。
     具体实现类（Concrete Implementor）：实现实现类接口的具体类。
"""


class Abstraction:
    def __init__(self, implementation):
        self.implementation = implementation

    def operation(self):
        return f"Abstraction: Base operation with:\n{self.implementation.operation_implementation()}"


class ExtendedAbstraction(Abstraction):
    def operation(self):
        return f"ExtendedAbstraction: Extended operation with:\n{self.implementation.operation_implementation()}"


class Implementation:
    def operation_implementation(self):
        pass


class ConcreteImplementationA(Implementation):
    def operation_implementation(self):
        return "ConcreteImplementationA: Here's the result on the platform A."


# Similar class ConcreteImplementationB

if __name__ == "__main__":
    ConcreteImplementationA = ConcreteImplementationA()
    print(ConcreteImplementationA.operation_implementation())
