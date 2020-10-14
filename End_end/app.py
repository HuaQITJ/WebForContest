'''

'''
from flask import Flask, request, session, redirect
from flask import jsonify
from flask_login import (LoginManager, login_required)

from flask_cors import CORS

app = Flask(__name__)

login_manager = LoginManager(app)
'''
设置登录视图的名称，如果一个未登录用户请求一个只有登录用户才能访问的视图，
则闪现一条错误消息，并重定向到这里设置的登录视图。
如果未设置登录视图，则直接返回401错误。
'''
login_manager.login_view = 'login'
'''
设置当未登录用户请求一个只有登录用户才能访问的视图时，闪现的错误消息的内容，
默认的错误消息是：Please log in to access this page.。
'''

login_manager.login_message = 'Unauthorized User'
'''
设置闪现的错误消息的类别
'''

login_manager.login_message_category = "info"


# return jsonify({1: 'Hello World!', 2: '张辉'})


@app.route('/')
def fuck():
    print('dasfsad')
    return 'dfsd'


CORS(app, resources=r'/*')


@app.route('/login', methods=['POST'])
def login():
    '''
    用于解决登陆问题的函数
    :return:
    '''
    data = request.get_json(silent=True)
    print(data)
    return 'dasf'
    # 中间在数据库中search一下

    # return jsonify({'Name': 'sfd', 'fdasf': 'dafasd'})


if __name__ == '__main__':
    # a = {'Name': '蔡若凡'}
    app.run()
