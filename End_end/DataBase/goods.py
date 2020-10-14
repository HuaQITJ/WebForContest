'''
定义商品类
'''


class Goods_infor:
    '''
    商品类
    这里似乎可以有列表属性
    '''

    def __init__(self, id, zhubo_id, name, price, sales_volume,):
        self.id = id
        self.zhubo_id = zhubo_id
        self.name = name
        self.price = price
        self.sales_volume = sales_volume

        # pass

    def keys(self):
        '''
        对象生成字典
        :return:
        '''
        return 'id', 'name', 'password', 'type'

    def __getitem__(self, item):
        '''
        对象生成字典
        :param item:
        :return:
        '''
        return getattr(self, item)
