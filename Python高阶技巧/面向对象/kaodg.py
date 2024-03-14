"""
    生命周期：一个对象，从诞生到消亡的过程。
            当一个对象被创建时，会在内存中分配相应的内存空间进行存储。当这个对象不在使用时，为了节约内存，就会把这个对象释放
    引用计算器：一个对象，会记录这自身被引用的个数，增加一个引用，加一，减少一个引用，减一，当引用个数为0时，系统会自动回收掉该内存
"""


class Digua:

    def __init__(self):
        self.status = 0
        self.num = 0
        self.maturity = '生的'
        print('挖了一个地瓜')

    def barbecue(self, barbecue_time):
        print('开始烤地瓜')
        self.num += barbecue_time
        if self.num < 3:
            self.maturity = '生的'
        elif 3 <= self.num < 6:
            self.maturity = '半生不熟'
        elif 6 <= self.num < 8:
            self.maturity = '熟了'
        else:
            self.maturity = '烤糊了'

    def __str__(self):
        return f'烧烤总时间：{self.num},成熟度：{self.maturity}'


if __name__ == '__main__':
    digua = Digua()
    for i in range(10):
        digua.barbecue(1)
        print(digua)
