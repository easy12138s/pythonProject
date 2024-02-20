"""
    作用域就是变量的作用范围，在哪里可以使用，在哪里不可以使用。
    Python中变量随着函数的出现，作用域可以划分两种情况：① 全局作用域 ② 局部作用域
    随着作用域的出现，变量也被强制划分两种类型：① 全局变量 ② 局部变量
    ① 全局变量：在全局作用域中定义的变量就是全局变量
    ② 局部变量：在局部作用域中定义的变量就是局部变量

    闭包特性示例
    1.外部函数中定义了一个内部函数
    2.外部函数总是返回内部函数的引用
    3.内部函数可以使用外部函数提供的环境变量

    闭包可以保存外部函数内的变量，不会随着外部函数调用完而销毁。 注意点: 由于闭包引用了外部函数的变量，则外部函数的变量没有及时释放，消耗内存。
"""


# 简单闭包
def outer(logo):
    def inner(msg):
        print(f"<{logo}>{msg}<{logo}>")

    return inner


fn = outer("easy")
fn("hi!")
fn("hi!")

fn2 = outer("jason")
fn2("hi!")


# nonlocal 修改外部函数值
# ATM机案例
def account_create(initial_amount=0):
    def atm(num, deposit=True):
        nonlocal initial_amount
        if deposit:
            initial_amount += num
            print(f"存款 : {num}元，账户余额：{initial_amount}")
        else:
            initial_amount -= num
            print(f"取款 : {num}元，账户余额：{initial_amount}")

    return atm


atm = account_create()
atm(100)
atm(100)
atm(50, deposit=False)


def outer():
    result = 0

    def inner(num):
        nonlocal result
        result += num
        print(result)

    return inner


f = outer()
f(1)
f(2)
f(3)  # 问这次的执行结果是多少？
