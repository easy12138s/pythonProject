"""
    数据分析案例文件读取相关的抽象类于实现
"""
import json

from date_define import Record


# 顶层设计,定义读取文件抽象类，确定需要实现哪些功能
class FileReader:

    def read_date(self) -> list[Record]:
        """读取文件的数据，读取到的每一条数据都是一个Record类对象，使用List进行封装"""
        pass


# 读取文本文件实现类
class TextFileReader(FileReader):

    def __init__(self, path):
        self.path = path  # 定义成员变量记录文件路径

    # 复写父类方法，实现读取文件
    def read_date(self) -> list[Record]:
        with open(self.path, "r", encoding="UTF-8") as f:
            record_list = []  # type: list[Record]
            for line in f.readlines():
                line = line.strip()  # 去除每一行读取到的换行符 \n
                date_list = line.split(",")  # type: list
                record = Record(date_list[0], date_list[1], int(date_list[2]), date_list[3])
                record_list.append(record)

        return record_list


# 读取JSON文件实现类
class JsonFileReader(FileReader):

    def __init__(self, path):
        self.path = path  # 定义成员变量记录文件路径

    # 复写父类方法，实现读取文件
    def read_date(self) -> list[Record]:
        with open(self.path, "r", encoding="UTF-8") as f:
            record_list = []  # type: list[Record]
            for line in f.readlines():
                date_dict = json.loads(line)
                record = Record(date_dict["date"], date_dict["order_id"], int(date_dict["money"]),
                                date_dict["province"])
                record_list.append(record)

        return record_list


if __name__ == '__main__':
    text = TextFileReader("E:/pythonProject/数据分析/2011年1月销售数据.txt")
    json1 = JsonFileReader("E:/pythonProject/数据分析/2011年2月销售数据JSON.txt")
    list1 = text.read_date()
    list2 = json1.read_date()

    for i in list1:
        print(i)

    for i in list2:
        print(i)

