"""
    装饰器也是一种闭包，功能是为了不破坏目标函数的前提下，为目标函数新增功能
    ①不修改已有函数的源代码
    ②不修改已有函数的调用方式
    ③给已有函数增加额外的功能

    装饰器函数通过接收一个函数参数传递给装饰器函数内部的嵌套函数，最后返回内部函数，其中内部函数大致分为原函数调用，调用前和调用后

"""

def outer(func):
    def inner():
        print("我睡觉了。。。")
        func()
        print("我起床了！")
    return inner


@outer
def sleep():
    import random
    import time
    print("睡眠中。。。")
    time.sleep(random.randint(1, 5))

sleep()


# 装饰带参数的函数或者是带返回值的函数，装饰器都要有相关体现，调用运用了装饰器的函数sum_num()其实就是调用装饰器函数inner()
def logging(fn):
    def inner(num1, num2):
        print('--正在努力计算--')
        fn(num1, num2)
    return inner

@logging
def sum_num(num1, num2):
    result = num1 + num2
    print(result)

sum_num(10, 20)

"""
    类装饰器的使用：通过定义一个类来装饰函数。
    
    这段代码定义了一个装饰器类 Check，用于在被装饰的函数执行前进行一些操作，
    例如检查用户是否已经登录。 在类的初始化方法 init 中，将被装饰的函数 fn 保存在实例属性 fn 中。
    
    在类中定义了一个特殊方法 call，该方法会在类实例像函数一样被调用时执行。在 call 方法中，先输出一条提示信息，然后调用保存在 fn 属性中的函数。
    
    
"""
class Check(object):
    def __init__(self, fn):
        # 初始化操作在此完成
        self.__fn = fn

    # 实现__call__方法，表示把类像调用函数一样进行调用。
    def __call__(self, *args, **kwargs):
        # 添加装饰功能
        print("请先登陆...")
        self.__fn()
@Check
def comment():
    print("发表评论")

comment()