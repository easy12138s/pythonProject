"""
    Pandas 提供了 reindex() 方法来执行重新索引操作。有以下常见的用法：

    更改现有索引的顺序：传入一个新的索引顺序，将数据按照新的索引顺序重新排序。
    增加缺失值或填充值：根据新的索引增加缺失值，或者使用指定的填充值填充缺失位置。
    修改行索引或列索引：修改行索引或列索引。
"""
import pandas as pd

# 创建一个示例 Series
s = pd.Series([1, 2, 3], index=['a', 'b', 'c'])
# 重新索引，按照新的索引顺序排序
s_reindexed = s.reindex(['c', 'b', 'a'])
print(s_reindexed)
# 重新索引，增加缺失值
s_reindexed = s.reindex(['a', 'b', 'c', 'd'])
print(s_reindexed)
# 重新索引，填充缺失位置为 0
s_filled = s.reindex(['a', 'b', 'c', 'd'], fill_value=0)
print(s_filled)
# 创建一个示例 DataFrame
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]}, index=['a', 'b', 'c'])
# 修改行索引
df_reindexed_rows = df.reindex(['c', 'b', 'a'])
print(df_reindexed_rows)
# 修改列索引
df_reindexed_columns = df.reindex(columns=['B', 'A'])
print(df_reindexed_columns)
