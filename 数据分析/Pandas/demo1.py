"""
    序列（Series） 是 Pandas 库中的一维标记数组，类似于带有标签的一维数组。它由两部分组成：索引（Index）和值（Value）。
        索引提供了对数据的标签，可以用于访问和操作数据。值是存储在序列中的实际数据。序列中的数据类型可以是数字、字符串、布尔值等。

    数据框（DataFrame） 是 Pandas 库中的二维表格型数据结构，类似于电子表格或 SQL 中的表。它由行索引和列索引组成，
        每列可以包含不同类型的数据。数据框可以看作是多个序列按照同样的索引组合而成的。数据框常用于处理和分析结构化的数据。

    _append() 方法：将一个 DataFrame 追加到另一个 DataFrame 的末尾。
    concat() 方法： 沿着指定的轴（默认沿行）连接多个 DataFrame。
    join() 方法： 基于索引或列的值进行连接，也可以使用 merge() 实现相同的功能。
    merge() 方法：基于共同的列或索引值进行连接，并可以指定不同类型的连接。
"""
import pandas as pd

df1 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
df2 = pd.DataFrame({'A': [5, 6], 'B': [7, 8]})

combined_df1 = df1._append(df2)		# 创建一个新的 DataFrame，其中包含 df1 和 df2 的行
combined_df2 = pd.concat([df1, df2], axis=0) # axis=0 表示沿着行方向组合
combined_df3 = pd.concat([df1, df2], axis=1) # axis=1 表示沿着列方向组合
df1 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]}, index=['a', 'b'])
df2 = pd.DataFrame({'C': [5, 6], 'D': [7, 8]}, index=['b', 'c'])
combined_df4 = df1.join(df2)		# 通过索引将 df1 和 df2 进行连接,没有匹配到的会显示NaN
df1 = pd.DataFrame({'ID': [1, 2], 'Name': ['Alice', 'Bob']})
df2 = pd.DataFrame({'ID': [2, 3], 'Age': [25, 30]})
combined_df5 = pd.merge(df1, df2, on='ID')		# 通过 'ID' 列将 df1 和 df2 进行连接,只显示匹配上的数据

print(combined_df4)
