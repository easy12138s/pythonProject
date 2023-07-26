"""
    RDD:弹性分布式数据集
    PySpark针对数据的处理，都是以RDD对象为载体
    数据计算案例2：各个城市的销售额排名、全部城市售卖的商品类别、 北京售卖的商品类别
"""
from pyspark import SparkContext, SparkConf
import json
import os
os.environ['PYSPARK_PYTHON'] = "D:/Python/python.exe"      # 标记python解释器地址，让spark找到

conf = SparkConf().setMaster("local[1]").setAppName("spark_app")
sc = SparkContext(conf=conf)

# 准备一个RDD读取文件内容
rdd = sc.textFile("E:/pythonProject/Spark/file/orders.txt")

# 处理数据格式，按|进行分割json
json_src_rdd = rdd.flatMap(lambda x: x.split("|"))

# 将处理过后的json数据转换为字典数据
dict_rdd = json_src_rdd.map(lambda x: json.loads(x))

# (城市， 销售额)
city_with_money = dict_rdd.map(lambda x: (x['areaName'], int(x['money'])))
city_result_rdd = city_with_money.reduceByKey(lambda a, b: a + b)
result1 = city_result_rdd.sortBy(lambda x: x[1], ascending=False, numPartitions=1)
print("各个城市的销售额排名: ", result1.collect())

# 全部商品类别
all_category = dict_rdd.map(lambda x: x['category']).distinct()
print("全部商品类别 :", all_category.collect())

# 北京的数据
beijing_rdd = dict_rdd.filter(lambda x: x['areaName'] == '北京').map(lambda x: x['category']).distinct()
print("北京的商品类别：", beijing_rdd.collect())

# 关闭pyspark程序
sc.stop()
