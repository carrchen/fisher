from flask import Flask, current_app, Request

app = Flask(__name__)

# ctx = app.app_context()
# ctx.push()
# a = current_app
# d = current_app.config['DEBUG']
# ctx.pop()

# with
# 实现了上下文协议的对象使用with
# 上下文管理器
# __enter__ __exit__
# 上下文表达式必须要返回一个上下文管理器
with app.app_context():
    a = current_app
    d = current_app.config['DEBUG']

# 文件读写
# try:
#     f = open(r'D;\t.txt')
#     print(f.read())
# finally:
#     f.close()
#
# with open(r'D:\t.txt') as f:
#     print(f.read())

# as后面是上下文管理器中__enter__的返回值

# 1. 连接数据库
# 2. sql
# 3. 释放资源


class MyResource:
    def __enter__(self):
        print('connect to resource')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_tb:
            print('process exception')
        else:
            print('no exception')
        print('close resource')
        return False

    def query(self):
        print('query data')


try:
    with MyResource() as resource:
        1/0
        resource.query()
except Exception as ex:
    pass
