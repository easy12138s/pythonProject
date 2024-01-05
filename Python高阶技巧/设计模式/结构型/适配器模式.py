# encoding: utf-8
"""
    @version: python3.1
    @author:'EASY'
    @contact: 2418087868@qq.com
    @software: PyCharm
    @file: 适配器模式.py
    @time: 2024/1/5 13:51
"""
# 适配器模式（Adapter Pattern）是作为两个不兼容的接口之间的桥梁。这种类型的设计模式属于结构型模式，它结合了两个独立接口的功能。

class A:
    def a(self):
        print("我是A类的a方法")


class B:
    def b(self):
        print("我是B类的b方法")


class C:
    def c(self):
        print("我是C类的c方法")


class Adapter:

    def __init__(self, classname, method):
        self.classname = classname
        self.__dict__update = method
    def __getattr__(self, attr):
        return getattr(self.classname, attr)



def test():
    objects = []
    AA = A()
    objects.append(Adapter(AA, dict(test=AA.a)))
    BB = B()
    objects.append(Adapter(BB, dict(test=BB.b)))
    CC = C()
    objects.append(Adapter(CC, dict(test=CC.c)))
    for obj in objects:
        obj.test()

test()