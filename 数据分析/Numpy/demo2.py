import numpy as np

# 多维度数组切片操作
# 数组维度转换- reshape，将数组转换为多维数组
t1 = np.arange(24).reshape(2, 3, 4)
print(t1)
print(t1[:, 0, 0])  # 两个数组块的第一行第一列的元素
print(t1[0, :, :])
print(t1[0, 1, ::2])
print(t1[..., 1])   # 第二列所有元素
print(t1[::-1])     # 翻转数组块顺序
print("*"*100)

# 数组的修改操作
# 将数组展开为一维数组--ravel\flatten
# ravel返回的是一个视图，flatten会使用内存空间对数组进行存储
print(t1.ravel())

print(t1.flatten())

# 直接使用shape也可以改变数组的维度
t1.shape = (6, 4)
print(t1)

# transpose转置数组，转换行列
print(t1.transpose())
print("*"*100)

# 数组组合方式
n1 = np.arange(6).reshape(2, 3)
n2 = np.arange(6).reshape(2, 3)
print("--------水平组合--------")
print(np.hstack((n1, n2)))
print("--------垂直组合--------")
print(np.vstack((n1, n2)))
# concatenate()可以实现水平和垂直组合效果
# concatenate((n1, n2), axis=1)-水平组合
# concatenate((n1, n2), axis=0)-垂直组合

print("--------深度组合--------")
print(np.dstack((n1, n2)))

print("--------行组合--------")
print(np.row_stack((n1, n2)))

print("--------列组合--------")
print(np.column_stack((n1, n2)))

# 数组分割常见方法-hsplit、vsplit、dsplit和split函数

