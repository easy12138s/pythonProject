# encoding: utf-8
"""
    @version: python3.1
    @author:'EASY'
    @contact: 2418087868@qq.com
    @software: PyCharm
    @file: demo5.py
    @time: 2023/11/7 16:52
"""
import pandas as pd
a = [1, 2, 4, 3, 6]
b = pd.DataFrame(a, columns=['one'])
print(b.sort_values('one'))