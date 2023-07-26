"""
    装饰器也是一种闭包，
    功能是为了不破坏目标函数的前提下，为目标函数新增功能
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
