"""
    在遇到CPU密集计算型计算时，多线程反而会降低执行速度

    多进程：运行多个python解释器进程
    语法和多线程几乎一样
"""
from multiprocessing import Process
from multiprocessing import Queue

# 池化技术
from concurrent.futures import ProcessPoolExecutor
from concurrent.futures import ThreadPoolExecutor

import math
import time

PRIMES = [99999923412131244211] * 10000


# 计算素数
def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    sqrt_n = int(math.floor(math.sqrt(n)))
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    return True


# 单线程模式
def single_thread():
    for number in PRIMES:
        is_prime(number)


# 多线程模式
def multi_thread():
    with ThreadPoolExecutor() as pool:
        pool.map(is_prime, PRIMES)


# 多进程模式
def multi_process():
    with ProcessPoolExecutor() as pool:
        pool.map(is_prime, PRIMES)


if __name__ == '__main__':
    start = time.time()
    single_thread()
    end = time.time()
    print('单线程执行时间：', end - start)

    start = time.time()
    multi_thread()
    end = time.time()
    print('多线程执行时间：', end - start)

    start = time.time()
    multi_process()
    end = time.time()
    print('多进程执行时间：', end - start)
