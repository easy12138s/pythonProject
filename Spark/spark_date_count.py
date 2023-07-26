"""
    热门搜索时段前三
    热门搜索词top3
    统计某一关键词在哪个时段搜多最多
    数据转换为JSON格式，写出为文件
"""
from pyspark import SparkContext, SparkConf
import json
import os
os.environ['PYSPARK_PYTHON'] = "D:/Python/python.exe"      # 标记python解释器地址，让spark找到

conf = SparkConf().setMaster("local[1]").setAppName("spark_app")
sc = SparkContext(conf=conf)

# 准备一个RDD读取文件内容
rdd = sc.textFile("E:/pythonProject/Spark/file/search_log.txt")

# 001-热门搜索时段前三
search_rdd_top3 = rdd.map(lambda x: (x.split("\t")[0][:2], 1)).\
    reduceByKey(lambda a, b: a + b).\
    sortBy(lambda x: x[1], ascending=False, numPartitions=1).\
    take(3)

print("热门搜索时段前三:", search_rdd_top3)

# 002-热门搜索词top3
word_rdd_top3 = rdd.map(lambda x: (x.split("\t")[2], 1)).\
                    reduceByKey(lambda a, b: a + b).\
                    sortBy(lambda x: x[1], ascending=False, numPartitions=1).\
                    take(3)
print("热门搜索词top3:", word_rdd_top3)

# 003-统计某一关键词在哪个时段搜多最多
heima_rdd_top = rdd.map(lambda x: x.split("\t")).\
                    filter(lambda x: x[2] == '黑马程序员').\
                    map(lambda x: (x[0][:2], 1)).\
                    reduceByKey(lambda a, b:a + b).\
                    sortBy(lambda x: x[1], ascending=False, numPartitions=1).\
                    take(1)
print("统计某一关键词在哪个时段搜多最多:", heima_rdd_top)

# 004-数据转换为JSON格式，写出为文件
rdd.map(lambda x: x.split("\t")).\
           map(lambda x: {"time": x[0], "user_id": x[1], "key_word": x[2], "rank1": x[3], "rank2": x[4], "url": x[5]}).\
           saveAsTextFile("E:/pythonProject/Spark/file/output.json")
