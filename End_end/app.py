from flask import Flask
from flask import jsonify

app = Flask(__name__)


@app.route('/crf')
def hello_world():
    return jsonify({1: 'Hello World!', 2: '张辉'})


@app.route('/')
def fuck():
    return 'dfsd'


@app.route('/search/<name>', methods=['GET'])
def search(name):
    # 中间在数据库中search一下
    return jsonify({'Name': name, 'fdasf': 'dafasd'})

app

if __name__ == '__main__':
    a = {'Name': '蔡若凡'}
    app.run()
