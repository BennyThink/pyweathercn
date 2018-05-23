#!/usr/bin/python
# coding:utf-8

# pyweathercn - helper.py
# 2018/5/22 16:32
# 

__author__ = 'Benny <benny@bennythink.com>'

from flask import Flask
from pyweathercn.craw import make_json

app = Flask(__name__)


def today(city):
    make_json(city)


@app.route("/")
def hello():
    return "Hello World!"


if __name__ == '__main__':
    app.run()
