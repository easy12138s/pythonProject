"""
    RDD:弹性分布式数据集
    PySpark针对数据的处理，都是以RDD对象为载体
    数据计算案例1：统计单词出现的次数
"""
from pyspark import SparkContext, SparkConf
import os
os.environ['PYSPARK_PYTHON'] = "D:/Python/python.exe"      # 标记python解释器地址，让spark找到

conf = SparkConf().setMaster("local[1]").setAppName("spark_app")
sc = SparkContext(conf=conf)

# 准备一个RDD
rdd = sc.textFile("E:/pythonProject/Spark/file/hello.txt")

# 聚合计算文件的所有单词数量
word_rdd = rdd.flatMap(lambda x: x.split(" "))
# 将数据转换为（key, 1）的形式，每个单词都是一个固定的key
word_one = word_rdd.map(lambda word: (word, 1))
word_result = word_one.reduceByKey(lambda a, b: a + b)

print(word_result.collect())
# 关闭pyspark程序
sc.stop()
