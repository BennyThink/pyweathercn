#!/usr/bin/python
# coding:utf-8

# pyweathercn - deco.py
# 2018/5/25 21:30
# 

__author__ = 'Benny <benny@bennythink.com>'

import logging

logging.basicConfig(level=logging.INFO)


def logger(fun):
    def wrapper(args):
        res = fun(args)
        logging.info(f'Testing {fun.__name__} now...')
        return res

    return wrapper
