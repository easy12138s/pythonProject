"""
    数据输出相比较于数据计算，数据输出调用算子后，返回的不是rdd

    saveAsTextFile(“文件路径”)
    输出结果是一个文件夹
    有多少分区就会生成多少个文件
    通过配置参数修改分区数--parallelize第二个参数设置1（rdd = sc.parallelize([1, 2, 3, 4, 5], numSlices=1)）
"""
from pyspark import SparkContext, SparkConf
import os
os.environ['PYSPARK_PYTHON'] = "D:/Python/python.exe"      # 标记python解释器地址，让spark找到

conf = SparkConf().setMaster("local[1]").setAppName("spark_app")
sc = SparkContext(conf=conf)

rdd = sc.parallelize([1, 2, 3, 4, 5], numSlices=1)
print(type(rdd.collect()))

rdd.saveAsTextFile("想要保存到的目录")  # 保存rdd到此路径

# reduce,对RDD进行两两聚合
rdd8 = sc.parallelize([1, 2, 3, 4, 5])
result8 = rdd8.reduce(lambda a, b: a + b)
print(result8)
print("-------reduce方法测试-------")

# take ，取出rdd前n个元素,返回一个list
print(rdd8.take(3))
print("-------take方法测试-------")

# count，统计rdd元素个数
print(rdd8.count())
print("-------count方法测试-------")
