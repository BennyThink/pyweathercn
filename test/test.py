#!/usr/bin/python
# coding:utf-8

# pyweathercn - test.py
# 2018/5/23 16:54
# 

__author__ = 'Benny <benny@bennythink.com>'

import pyweathercn

pyweathercn.Weather('重庆').temp()

w = pyweathercn.Weather('北京')

print(w.forecast(False,3))