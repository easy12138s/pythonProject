# encoding: utf-8
"""
    @version: python3.1
    @author:'EASY'
    @contact: 2418087868@qq.com
    @software: PyCharm
    @file: 常见语法糖.py
    @time: 2023/11/9 13:56
"""
# 定义数值变量时，可以用_分割，便于理解
# a = 10_0000_0000
# print(a)  # 1000000000

# 交换两个变量的值
# a = 10
# b = 5
# a, b = b, a
# print(a)  # 5
# print(b)  # 10

# 判断变量是否在某个范围内
# a = 88
# if a >= 50 <= 100:
#     print(a)

# 快速构造字符串
# print('-' * 60)
# print('%' * 10)

# 列表拼接
# a = [1,2,3]
# b = [1,2,3,4,5,6]
# print(a + b)

# 列表切片
# a = [1, 2, 3, 4, 5, 6]
# print(a[2: -2])

# 打包与解包
# a = (1, 2, 3)
# x, y, z = a
# b = x, y, z
# print(b)

# with语句,常用于文件操作
# with open('多线程.py', 'r') as f:
#     data = f.readlines()

# 列表推导式
# a = [1, 2, 3, 4, 5, 6]
# b = [i+123 for i in a]
# print(b)
