from flask import Flask
from flask import jsonify

app = Flask(__name__)


@app.route('/')
def hello_world():
    return jsonify({1: 'Hello World!', 2: '张辉'})


if __name__ == '__main__':
    app.run()



