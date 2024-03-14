"""
    通过使用@staticmethod装饰器和@classmethod装饰器，我们可以在Python中直接调用类方法。

    类方法可以使用类的属性和方法，但不能访问实例的属性和方法。
    静态方法是定义在类上的方法，它可以通过类或者类的实例来调用。
        静态方法使用@staticmethod装饰器进行标识，它不需要类或实例作为第一个参数。与类方法不同，静态方法不能访问类或实例的属性和方法。
"""


class MyClass:
    __count = 0
    num = 0

    def __init__(self):
        self.count = 0
        MyClass.__count += 1
        self.count += 1

    @classmethod
    def get_count(cls):
        return cls.__count

    @classmethod
    def set_count(cls, num):
        cls.__count += num
        return cls.__count

    @classmethod
    def set_count1(cls, self):
        cls.num = 1
        self.num = 2
        print(f'类变量：{cls.num},对象变量： {self.num}')
        return 1


a = MyClass()
print(a.count, a.__hash__(), a.set_count1(a))
b = MyClass()
print(b.count, b.__hash__())
c = MyClass()
print(c.count, c.__hash__())
print(MyClass.get_count())
print(MyClass.set_count(1))


class MyClass:

    @classmethod
    def my_class_method(cls, arg1, arg2):
        print("Class method called with args:", arg1, arg2)

# MyClass.my_class_method(1, 2)
# # 输出：Class method called with args: 1 2
#
# obj = MyClass()
# obj.my_class_method(3, 4)
# # 输出：Class method called with args: 3 4
