# encoding: utf-8
"""
    @version: python3.1
    @author:'EASY'
    @contact: 2418087868@qq.com
    @software: PyCharm
    @file: leetcode.py
    @time: 2023/11/3 15:34
"""
import pandas as pd


# # 2877
# def createDataframe(student_data: list[list[int]]) -> pd.DataFrame:
#     student_data_pd = pd.DataFrame(student_data, columns=['student_id', 'age'])
#     return student_data_pd
#
# if __name__ == '__main__':
#     student_data_list = [[1, 15],[2, 11],[3, 11],[4, 20]]
#     print(createDataframe(student_data_list))

# # 2878
# def getDataframeSize(players: pd.DataFrame) -> list[int]:
#     size_list = [players.shape[0], players.shape[1]]
#     return size_list
#
# if __name__ == '__main__':
#     student_data_list = [[1, 15],[2, 11],[3, 11],[4, 20]]
#     df = pd.DataFrame(student_data_list)
#     print(getDataframeSize(df))

# # 2879
# def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
#     return employees.head(3)

# # 2880
# def selectData(students: pd.DataFrame) -> pd.DataFrame:
#     return students.loc[students['student_id'] == 101, ['name', 'age']]

# # 2881
# def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
#     employees['bonus'] = employees['salary'] * 2
#     return employees

# # 2882
# def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
#     return customers.drop_duplicates(subset='email', keep='first')

# # 2883
# def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
#     return students.dropna(subset='name')

# # 2884
# def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
#     employees['salary'] = employees['salary'] * 2
#     return employees

# # 2885
# def renameColumns(students: pd.DataFrame) -> pd.DataFrame:
#     students.columns = ['student_id', 'first_name', 'last_name', 'age_in_years']
#     return students

# # 2886
# def changeDatatype(students: pd.DataFrame) -> pd.DataFrame:
#     students['grade'] = students['grade'].astype(int)
#     # students['grade'] = students['grade'].apply(lambda x:int(x))
#     return students

# # 2887
# def fillMissingValues(products: pd.DataFrame) -> pd.DataFrame:
#     products['quantity'].fillna(0, inplace=True)
#     return products

# # 2888
# def concatenateTables(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
#     return pd.concat([df1, df2], ignore_index=True)

# # 2889
# def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
#     return weather.pivot(index='month', columns='city', values='temperature ')

# # 2890
# def meltTable(report: pd.DataFrame) -> pd.DataFrame:
#     reshaped_report = pd.melt(report, id_vars=['product'], var_name='quarter', value_name='sales')
#     return reshaped_report

# 2891
def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    return animals.loc[animals.weight > 100].sort_values(by='weight', ascending=False)[['name']]
