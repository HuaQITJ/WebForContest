from flask_sqlalchemy import SQLAlchemy
# from SQLAlchemy import Colunm,
import sqlalchemy
from sqlalchemy import create_engine, Column, String, Date, Integer, Enum, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

HOSTNAME = '127.0.0.1'
PORT = 3306
DATABASE = 'huaqi'
USERNAME = 'root'
PASSWORD = '010095cb'

DB_URI = 'mysql+pymysql://{username}:{password}@{host}:{port}/{dbname}?charset=utf8'. \
    format(
    username=USERNAME,
    password=PASSWORD,
    host=HOSTNAME,
    port=PORT,
    dbname=DATABASE
)

engine = create_engine(DB_URI, echo=True)  # 显示sql语句
Base = declarative_base(engine)
Session = sessionmaker(engine)
session = Session()


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(60))
    password = Column(String(60))
    type = Column(Enum('企业用户', '主播用户'), server_default='主播用户', nullable=False)

    def __init__(self, id=None, name=None, password=None, type=None):
        self.id = id
        self.name = name
        self.password = password
        self.type = type

    # 该函数用于对象的实例化输出，其调用的就是该对象的 __repr__() 方法，输出的是该方法的返回值。
    def __repr__(self) -> str:
        # return '<User id:%r name:%r password:%r type%r >' % (
        #     self.id,
        #     self.name,
        #     self.password,
        #     self.type)
        # 这个方法只能返回一个字符串，不能返回一个字典类型
        # 这里必须将字符串向字典进行转化
        # %r是万能输出符，可以将后面的内容原封不动的打印出来
        return '{"id":%r,"name":%r,"password":%r,"type":%r}' % (
            self.id,
            self.name,
            self.password,
            self.type
        )

    def keys(self):
        return 'id', 'name', 'password', 'type'

    def __getitem__(self, item):
        return getattr(self, item)


class Up_Infor(Base):
    __tablename__ = 'up_infor'
    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(60))
    comments_count = Column(Integer)
    fans = Column(Integer)
    goods_comments = Column(Integer)  # 带的商品的数量
    zans = Column(Integer)  # 点赞的数量
    introduce = Column(String(100))

    # def
    def __repr__(self):
        pass

    def keys(self):
        return 'id', 'name', 'comments_count', 'fans', 'goods_comments', 'zans', 'introduce'

    def __getitem__(self, item):
        return getattr(self, item)


# 记录企业与up主的关系
# 两个外键作为联合主键，两个id确定一条唯一的纪录(不对这玩意)
class Contract(Base):
    __tablename__ = 'contract'
    Contract_id = Column(Integer, primary_key=True, autoincrement=True)
    up_id = Column(Integer, ForeignKey('up_infor.id'))
    user_id = Column(Integer, ForeignKey('user.id'))

    # db.PrimaryKeyConstraint(up_id, user_id)

    def __repr__(self):
        pass

    def keys(self):
        return 'Contract_id', 'up_id', 'user_id'

    def __getitem__(self, item):
        return getattr(self, item)


if __name__ == '__main__':
    pass
