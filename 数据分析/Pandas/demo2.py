"""
    识别缺失值：使用 Pandas 库中的 isna() 或 isnull() 函数可以对 DataFrame 进行逐个元素的遍历，并返回一个布尔类型的 DataFrame，
    其中的 True 表示该位置存在缺失值。
"""
import pandas as pd

# 创建一个包含缺失值的 DataFrame
df = pd.DataFrame({'A': [1, 2, None, 4],
                   'B': [5, None, 7, 8],
                   'C': [9, 10, 11, None]})

# 判断每个元素是否为缺失值
is_missing = df.isnull()
print(is_missing)

# 删除包含缺失值的行
df_dropna = df.dropna()
print(df_dropna)

# 删除包含缺失值的列
df_dropna_columns = df.dropna(axis=1)
print(df_dropna_columns)

# 将缺失值替换为 0
df_fillna = df.fillna(0)
print(df_fillna)

# 将缺失值替换为每列的平均值
df_fillna_mean = df.fillna(df.mean())
print(df_fillna_mean)
