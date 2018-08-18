#!/usr/bin/python
# coding: utf-8

# pyweathercn - utils.py
# 2018/8/18 15:12
# decorator utilities, for API Key authentication and so on

__author__ = "Benny <benny@bennythink.com>"


def require_api(fun):
    def wrapper(self):
        res = fun(self)
        # TODO: add API Key here...
        print('TBC')
        return res

    return wrapper
