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


"""
    Customers 表：
    +-------------+---------+
    | Column Name | Type    |
    +-------------+---------+
    | id          | int     |
    | name        | varchar |
    +-------------+---------+
    在 SQL 中，id 是该表的主键。
    该表的每一行都表示客户的 ID 和名称。
    Orders 表：
    +-------------+------+
    | Column Name | Type |
    +-------------+------+
    | id          | int  |
    | customerId  | int  |
    +-------------+------+
    在 SQL 中，id 是该表的主键。
    customerId 是 Customers 表中 ID 的外键( Pandas 中的连接键)。
    该表的每一行都表示订单的 ID 和订购该订单的客户的 ID。
    
    找出所有从不点任何东西的顾客。
"""


def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    world = pd.merge(customers, orders, how='outer', left_on='id', right_on='customerId')
    world['customers'] = world[world.isnull().any(axis=1)][['name']]
    return world[['customers']].dropna()


"""
    Views 表：
    +---------------+---------+
    | Column Name   | Type    |
    +---------------+---------+
    | article_id    | int     |
    | author_id     | int     |
    | viewer_id     | int     |
    | view_date     | date    |
    +---------------+---------+
    此表可能会存在重复行。（换句话说，在 SQL 中这个表没有主键）
    此表的每一行都表示某人在某天浏览了某位作者的某篇文章。
    请注意，同一人的 author_id 和 viewer_id 是相同的。

    请查询出所有浏览过自己文章的作者
    结果按照 id 升序排列。
    
    输入：
    Views 表：
    +------------+-----------+-----------+------------+
    | article_id | author_id | viewer_id | view_date  |
    +------------+-----------+-----------+------------+
    | 1          | 3         | 5         | 2019-08-01 |
    | 1          | 3         | 6         | 2019-08-02 |
    | 2          | 7         | 7         | 2019-08-01 |
    | 2          | 7         | 6         | 2019-08-02 |
    | 4          | 7         | 1         | 2019-07-22 |
    | 3          | 4         | 4         | 2019-07-21 |
    | 3          | 4         | 4         | 2019-07-21 |
    +------------+-----------+-----------+------------+
    
    输出：
    +------+
    | id   |
    +------+
    | 4    |
    | 7    |
    +------+
"""


def article_views(views: pd.DataFrame) -> pd.DataFrame:
    views = views[views['author_id'] == views['viewer_id']]
    return views


if __name__ == '__main__':
    world1 = pd.read_csv('./datafile/views.csv')
    print(article_views(world1))
