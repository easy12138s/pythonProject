from pyspark import SparkConf, SparkContext

"""
    PySpark编程模型： 数据输入、数据处理计算、数据输出
"""


# 创建SparkConf类对象,
# local为本地地址 可替换为集群地址，
# test_app_spark为程序命名
conf = SparkConf().setMaster("local[*]").setAppName("test_app_spark")

# 基于conf对象创建SparkContext对象,
# SparkContext对象是pyspark程序的入口
sc = SparkContext(conf=conf)

# 打印pyspark版本
print(sc.version)

# 关闭pyspark程序
sc.stop()


