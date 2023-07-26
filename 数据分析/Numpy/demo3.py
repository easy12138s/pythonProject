"""
    Numpy常用函数
"""
import numpy as np

# 单位矩阵：主对角线为1
n1 = np.eye(2)
print(n1)

# 保存数组到文件里 savetxt
np.savetxt("./file/eye1.txt", n1)

# 读取CSV文件使用loadtxt函数：
c, v = np.loadtxt('data.csv', delimiter=',', usecols=(6, 7), unpack=True)
# usecols的参数为一个元组，获取第7字段至第8字段的数据。
# unpack参数设置为True，意思是分拆存储不同列的数据，即分别将7字段和8字段的数组赋值给变量c和v
# delimiter表示数据按‘，’进行分割




