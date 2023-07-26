"""
    RDD:弹性分布式数据集
    PySpark针对数据的处理，都是以RDD对象为载体

    使用textFile()方法读取文件路径
"""
from pyspark import SparkContext, SparkConf

conf = SparkConf().setMaster("local[*]").setAppName("spark_app")
sc = SparkContext(conf=conf)

# 读取文件，加载文件数据到RDD中
rdd = sc.textFile("E:/pythonProject/Spark/file/hello.txt")

print(rdd.collect())

# 关闭spark程序
sc.stop()
