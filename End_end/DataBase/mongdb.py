# from flask_pymongo import PyMongo
'''
MongoDB的操作文件
'''
import pymongo


# 最后的名称要落实到数据库
# mongo = pymongo.MongoClient('mongodb://localhost:27017/')

# 面向对象的设计思想
class MongoManger:
    '''
    专用于管理网站的MongoDB事务,
    这有一个问题是，如何使用数据库检索通过主播找到货
    以及反过来如何通过货找到主播
    '''

    def __init__(self):
        self.mongo = pymongo.MongoClient('mongodb://localhost:27017/')
        self.database = self.mongo['huaqi']  # 建立数据库并命名
        self.goods = self.database['goods']  # 在数据库中建立商品集合

    def insert_data(self):
        '''
        向mongoDB中插入数据
        :return:
        '''

    # pass


if __name__ == '__main__':
    pass
