"""
    RDD:弹性分布式数据集
    PySpark针对数据的处理，都是以RDD对象为载体
"""
from pyspark import SparkContext, SparkConf

conf = SparkConf().setMaster("local[*]").setAppName("spark_app")
sc = SparkContext(conf=conf)

# 通过parallelize方法将python对象加载到Spark内，成为RDD对象
rdd1 = sc.parallelize([1, 2, 3, 4, 5])
rdd2 = sc.parallelize((1, 2, 3, 4, 5))
rdd3 = sc.parallelize("abcdefg")
rdd4 = sc.parallelize({1, 2, 3, 4, 5})
rdd5 = sc.parallelize({"key1": "value1", "key2": "value2"})

# 通过rdd的collect方法查看rdd内容
print(rdd1.collect())
print(rdd2.collect())
print(rdd3.collect())
print(rdd4.collect())
print(rdd5.collect())

sc.stop()
