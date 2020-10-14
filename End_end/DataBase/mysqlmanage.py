from DataBase.tables import db, User, Up_Infor, Contract
from flask import jsonify
import ast
import json


# from  DataBase.tables import

class MySqlManager:

    def __init__(self, Database):
        self.database = Database
        self.database.drop_all()
        self.database.create_all()

    def add_new_user(self):
        '''
        dsafsad
        :return:
        '''
        t = User(name='张辉', password='123456', type='企业用户')
        db.session.add(t)  #
        db.session.commit()  # 这一句pyCharm没有代码提示,先add再commit
        # db.session.

    def search_user(self):
        t = User(name='张辉', password='123456', type='企业用户')
        row = db.session.query(User).filter_by(name='张辉').all()

        print(type((row[0])))  #
        for t in row:
            if isinstance(t, User):
                print(dict(row[0]))

        pass


if __name__ == '__main__':
    t = MySqlManager(db)
    t.add_new_user()
    t.search_user()
# test = {"id": 1, "name": '张辉', "password": '123456', "type": '企业用户'}


# print(r)
