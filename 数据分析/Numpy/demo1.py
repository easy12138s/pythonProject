import numpy as np
import random

# 使用Numpy生成数组，数组类型ndarray
a = np.array([1, 2, 3, 4])
print(a[::-1])      # 翻转数组
print(type(a))

# a2 = np.array(range(10))
# print(a2)

a3 = np.arange(2, 10, 2)
print(a3)
print(a3.dtype)     # int32-表示是32位的电脑

# 指定数组类型
a4 = np.array(range(10), dtype=float)
print(a4)
print(a4.dtype)
print("*" * 100)

# round,保留两位小数
a5 = np.array([random.random() for i in range(10)])
print(a5)
print(np.round(a5, 2))
print("*" * 100)

# 数组属性
n1 = np.array(range(24)).reshape(2, 3, 4)
print(n1.ndim)      # 数组维度
print(n1.size)      # 数组大小
print(n1.itemsize)  # 数组元素所占字节大小
print(n1.nbytes)    # 整个数组所占的存储空间 = size * itemsize


