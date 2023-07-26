"""
    闭包特性示例

    1.外部函数中定义了一个内部函数
    2.外部函数总是返回内部函数的引用
    3.内部函数可以使用外部函数提供的环境变量
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
