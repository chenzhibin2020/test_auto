# -*- coding: utf-8 -*-
"""
@File    : flask_case01.py
@Author  : chenzhibin
@Time    : 2023/5/29 13:00
"""
# 程序说明:  首个flask 服务，验证flask 如何工作
# 程序结果: 是否报错：xx，是否拿到结果：xx


from flask import Flask

app = Flask(__name__)

@app.route("/")
def flask_server():
    print("Hello world!")
    return "Hello world!"

if __name__ == '__main__':
    app.run()

# WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.