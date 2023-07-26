"""
    某些场景需要一个类，无论获取多少实例对象，都只提供一个具体的实例
    比如一些工具类、、、，目的节省资源
    定义：保证一个类只有一个实例，并提供一个访问它的全局访问点
"""


# class StrTools:
#     pass
#
# s1 = StrTools()
# s2 = StrTools()
#
# print(id(s1), id(s2))

from StrTools import str_tools

s1 = str_tools
s2 = str_tools

print(id(s1))       # 1710073595600
print(id(s2))       # 1710073595600
