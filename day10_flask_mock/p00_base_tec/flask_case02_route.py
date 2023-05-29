# -*- coding: utf-8 -*-
"""
@File    : flask_case02_route.py
@Author  : chenzhibin
@Time    : 2023/5/29 13:12
"""
# 程序说明: 
# 程序结果: 是否报错：xx，是否拿到结果：xx

from flask import Flask

app = Flask(__name__)

@app.route('/<name>')
def flask_server(name):
    print(f"{name}: Hello world!  ")

    return f"Weclome to visit {name}"

if __name__ == '__main__':
    app.run()