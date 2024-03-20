import pandas as pd

"""
    595-大的国家
    
    如果一个国家满足下述两个条件之一，则认为该国是 大国 ：

    面积至少为 300 万平方公里（即，3000000 km2），或者
    人口至少为 2500 万（即 25000000）
    编写解决方案找出 大国 的国家名称、人口和面积。
    +-------------+-----------+---------+------------+--------------+
    | name        | continent | area    | population | gdp          |
    +-------------+-----------+---------+------------+--------------+
    | Afghanistan | Asia      | 652230  | 25500100   | 20343000000  |
    | Albania     | Europe    | 28748   | 2831741    | 12960000000  |
    | Algeria     | Africa    | 2381741 | 37100000   | 188681000000 |
    | Andorra     | Europe    | 468     | 78115      | 3712000000   |
    | Angola      | Africa    | 1246700 | 20609294   | 100990000000 |
    +-------------+-----------+---------+------------+--------------+
"""


def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    world = world[(world['area'] >= 3000000) | (world['population'] >= 25000000)]
    return world[['name', 'population', 'area']]


"""
    1757-可回收且低脂的产品
    
    编写解决方案找出既是低脂又是可回收的产品编号。
    返回结果 无顺序要求 。
    
    product_id 是该表的主键（具有唯一值的列）。
    low_fats 是枚举类型，取值为以下两种 ('Y', 'N')，其中 'Y' 表示该产品是低脂产品，'N' 表示不是低脂产品。
    recyclable 是枚举类型，取值为以下两种 ('Y', 'N')，其中 'Y' 表示该产品可回收，而 'N' 表示不可回收。
    输入：
    Products 表：
    +-------------+----------+------------+
    | product_id  | low_fats | recyclable |
    +-------------+----------+------------+
    | 0           | Y        | N          |
    | 1           | Y        | Y          |
    | 2           | N        | Y          |
    | 3           | Y        | Y          |
    | 4           | N        | N          |
    +-------------+----------+------------+
    输出：
    +-------------+
    | product_id  |
    +-------------+
    | 1           |
    | 3           |
    +-------------+
    解释：
    只有产品 id 为 1 和 3 的产品，既是低脂又是可回收的产品。
"""


def find_products(products: pd.DataFrame) -> pd.DataFrame:
    products = products[(products['low_fats'] == 'Y') & (products['recyclable'] == 'Y')]
    return products[['product_id']]


if __name__ == '__main__':
    world1 = pd.read_csv('./datafile/products.csv')
    print(find_products(world1))
