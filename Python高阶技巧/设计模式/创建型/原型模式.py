# encoding: utf-8
"""
    @version: python3.1
    @author:'EASY'
    @contact: 2418087868@qq.com
    @software: PyCharm
    @file: 原型模式.py
    @time: 2024/1/5 9:57
"""
# 原型模式（Prototype Pattern）是用于创建重复的对象，同时又能保证性能。这种类型的设计模式属于创建型模式，它提供了一种创建对象的最佳方式之一。

import copy


class Information:
    """个人信息"""

    def __init__(self):
        self.name = None
        self.ager = None
        self.height = None

    def run(self):
        """
        自我介绍方法
        :return:
        """
        print("我叫{}： 年龄：{} 身高：{}".format(self.name, self.ager, self.height))


class Prototype:
    def __init__(self, obj):
        self.copy_object = obj()

    def clone(self, **attr):
        obj = copy.deepcopy(self.copy_object)
        obj.__dict__.update(attr)
        return obj


if __name__ == '__main__':
    test = Prototype(Information)
    a = test.clone(name='张山', ager="30", height='170cm')
    a.run()
    b = test.clone(name='李飞', ager="20", height='190cm')
    b.run()