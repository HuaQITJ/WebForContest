from flask_sqlalchemy import SQLAlchemy

from app import app

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:010095cb@127.0.0.1:3306/huaqi'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)


class User(db.Model):
    __tablename_ = 'User'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(60))
    password = db.Column(db.String(60))
    type = db.Column(db.Enum('企业用户', '主播用户'), server_default='主播用户', nullable=False)

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


class Up_Infor(db.Model):
    __tablename__ = 'up_infor'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(60))
    comments_count = db.Column(db.Integer)
    fans = db.Column(db.Integer)
    goods_comments = db.Column(db.Integer)  # 带的商品的数量
    zans = db.Column(db.Integer)  # 点赞的数量
    introduce = db.Column(db.String(100))

    # def
    def __repr__(self):
        pass

    def keys(self):
        return 'id', 'name', 'comments_count', 'fans', 'goods_comments', 'zans', 'introduce'

    def __getitem__(self, item):
        return getattr(self, item)


# 记录企业与up主的关系
# 两个外键作为联合主键，两个id确定一条唯一的纪录(不对这玩意)
class Contract(db.Model):
    __tablename__ = 'contract'
    Contract_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    up_id = db.Column(db.Integer, db.ForeignKey('up_infor.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    # db.PrimaryKeyConstraint(up_id, user_id)

    def __repr__(self):
        pass

    def keys(self):
        return 'Contract_id', 'up_id', 'user_id'

    def __getitem__(self, item):
        return getattr(self, item)


if __name__ == '__main__':
    pass
