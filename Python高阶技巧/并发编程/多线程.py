"""
    threading
"""
import threading
import time


def sing():
    while True:
        print("我在唱歌，啦啦啦啦")
        time.sleep(1)


def dance():
    while True:
        print("我在跳舞，哒哒哒哒")
        time.sleep(1)


if __name__ == '__main__':
    # 唱歌线程
    thread_sing = threading.Thread(target=sing)     # args:以元组形式传参，kwargs：以字典形式传参
    # 跳舞线程
    thread_dance = threading.Thread(target=dance)

    # 开启线程
    thread_sing.start()
    thread_dance.start()
