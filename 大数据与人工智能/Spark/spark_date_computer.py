"""
    RDD:弹性分布式数据集
    PySpark针对数据的处理，都是以RDD对象为载体
"""
from pyspark import SparkContext, SparkConf
import os
os.environ['PYSPARK_PYTHON'] = "D:/Python/python.exe"      # 标记python解释器地址，让spark找到

conf = SparkConf().setMaster("local[1]").setAppName("spark_app")
sc = SparkContext(conf=conf)

# 准备一个RDD
rdd = sc.textFile("E:/pythonProject/Spark/file/hello.txt")
rdd1 = sc.parallelize([1, 2, 3, 4, 5])

# 定义函数供map方法调用
# def func(data):
#    return data * 10
#
# rdd2 = rdd1.map(func)

# 通过map将rdd1数据都×10，再+5
rdd2 = rdd1.map(lambda x: x * 10).map(lambda x: x + 5)  # 链式调用
print(rdd2.collect())
print("-------map方法测试-------")

# flatMap方法比map多了一个解除嵌套的功能
rdd3 = sc.parallelize([["a b c", 2, 3, 4], [5, 6, 7, 8]])
rdd3.flatMap(lambda x: x.split())
print(rdd3.collect())
print("-------flatMap方法测试-------")

# reduceByKey 对rdd分组，根据分组key对value进行聚合
rdd4 = sc.parallelize([('男', 99), ('男', 88), ('女', 99), ('女', 66)])
result = rdd4.reduceByKey(lambda a, b: a + b)
print(result.collect())
print("-------reduceByKey方法测试-------")

# filter方法，对rdd数据进行过滤,将自定义过滤逻辑函数返回的True的数据保留
rdd5 = sc.parallelize([1, 2, 3, 4, 5])
result5 = rdd5.filter(lambda num: num % 2 == 0)
print(result5.collect())
print("-------filter方法测试-------")

# distinct，去重
rdd6 = sc.parallelize([1, 2, 3, 4, 5, 1, 2, 3, 9])
result6 = rdd6.distinct()
print(result6.collect())
print("-------distinct方法测试-------")

# sortBy排序算法，传入函数的返回值是什么，就按哪个元素排序
rdd7 = sc.textFile("E:/pythonProject/Spark/file/hello.txt")
# 聚合计算文件的所有单词数量
word_rdd = rdd.flatMap(lambda x: x.split(" "))
# 将数据转换为（key, 1）的形式，每个单词都是一个固定的key
word_one = word_rdd.map(lambda word: (word, 1))
word_result = word_one.reduceByKey(lambda a, b: a + b)

result7 = word_result.sortBy(lambda x: x[1], ascending=False, numPartitions=1)  # ascending=False 降序， ascending=True  升序
print(result7.collect())
print("-------sortBy方法测试-------")

# 关闭pyspark程序
sc.stop()
