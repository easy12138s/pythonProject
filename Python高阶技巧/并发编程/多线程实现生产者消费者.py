"""
    queue.Queue(队列)用于多线程之间的、线程安全的数据通信

    import queue
    item = 'a'
    # 创建Queue
    q = queue.Queue()
    # 添加元素
    q.put(item)
    # 获取元素
    item = q.get()
    # 查看元素的多少
    q.qsize()
    # 判断是否为空
    q.empty()
    # 判断是否已满
    q.full()

    线程安全：指某个函数、函数库在多线程环境中被调用时，能够正确的处理多个线程之间的共享变量，使程序功能正常完成。
    线程不安全：由于线程的执行随时会发生切换，就造成了不可预料的结果，出现线程不安全。

    使用Lock加锁来保证线程安全
"""

# 线程不安全例子

# import threading
# import time
#
#
# class Account:
#     def __init__(self, balance):
#         self.balance = balance
#
#
# def draw(account, amount):
#     if account.balance >= amount:
#         time.sleep(0.1)     # 会导致当前线程阻塞，进而发生线程切换，来模拟线程冲突的情况
#         print(threading.current_thread().name, "取钱成功")
#         account.balance -= amount
#         print(threading.current_thread().name, "余额", account.balance)
#     else:
#         print(threading.current_thread().name, "取钱失败，余额不足")
#
#
# if __name__ == "__main__":
#     account = Account(1000)
#     ta = threading.Thread(name='ta', target=draw, args=(account, 800))
#     tb = threading.Thread(name='tb', target=draw, args=(account, 800))
#
#     ta.start()
#     tb.start()
#
#     tatb 取钱成功
#     tb 取钱成功
#     ta 余额 -600
#     余额 200


import threading
import time

lock = threading.Lock()


class Account:
    def __init__(self, balance):
        self.balance = balance


def draw(account: Account, amount):
    # 使用线程锁确保线程安全
    with lock:
        if account.balance >= amount:
            time.sleep(0.1)  # 会导致当前线程阻塞，进而发生线程切换，来模拟线程冲突的情况
            print(threading.current_thread().name, "取钱成功")
            account.balance -= amount
            print(threading.current_thread().name, "余额", account.balance)
        else:
            print(threading.current_thread().name, "取钱失败，余额不足")


if __name__ == "__main__":
    account = Account(1000)
    ta = threading.Thread(name='ta', target=draw, args=(account, 800))
    tb = threading.Thread(name='tb', target=draw, args=(account, 800))

    ta.start()
    tb.start()
    """
    ta 取钱成功
    ta 余额 200
    tb 取钱失败，余额不足
    """
