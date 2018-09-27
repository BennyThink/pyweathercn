#!/usr/bin/python
# coding: utf-8

# pyweathercn - utils.py
# 2018/8/18 15:12
# decorator utilities, for API Key authentication and so on

__author__ = "Benny <benny@bennythink.com>"

import json
import sqlite3
import time

from pyweathercn.constant import CODE

DB = ":memory:"


class RequireApi:
    def __init__(self, k):
        if DB == ":memory:" or DB is None:
            # disable auth
            self.__auth = False
            self.__msg = None
            self.__key = None
        elif k is None:
            # missed key
            self.con = sqlite3.connect(DB)
            self.cur = self.con.cursor()
            self.__auth = True
            self.__msg = {"status": 6, "message": CODE.get(6)}
            self.__key = None
        else:
            self.con = sqlite3.connect(DB)
            self.cur = self.con.cursor()
            self.__auth = True
            self.__msg = None
            self.__key = k

    def __del__(self):
        if self.__auth:
            self.con.close()

    def auth(self):
        # return True(contine) or False

        if not self.__auth:
            v = (True, None)
        else:
            self.cur.execute('SELECT times,restrict FROM auth WHERE key=?', (self.__key,))
            data = self.cur.fetchall()

            if data and data[0][1] == 0:
                # unlimited user
                v = (True, None)
            elif data and data[0][0] >= 1:
                # valid, limited user. we need to decrease.
                self.cur.execute('UPDATE auth SET times=? WHERE key=?', (data[0][0] - 1, self.__key))
                self.con.commit()
                v = (True, None)
            elif data and data[0][0] <= 0:
                # exceed
                v = (False, {"status": "error", "message": CODE.get(7)})
            else:
                # invalid key provided
                v = (False, {"status": "error", "message": CODE.get(6)})

        return v

    @staticmethod
    def get_key(s):
        # get parameter, compatibility with json
        if s.request.headers.get('Content-Type') == 'application/json':
            data = json.loads(s.request.body)
            key = data.get('key')
        else:
            key = s.get_argument('key', None)

        return key


def api(fun):
    def wrapper(self):
        key = RequireApi.get_key(self)
        k, msg = RequireApi(key).auth()
        if k:
            res = fun(self)
            return res
        else:
            self.write(msg)

    return wrapper


class TestCache:
    def __init__(self, timeout):
        # use redis, maybe
        pass

    def __del__(self):
        pass

    def test(self, city):
        # true: return db data
        # false: run requests
        pass

    def update(self, city, weather):
        pass


def cache(timeout):
    def func(fun):
        def inner(*args):
            t = TestCache(timeout)
            valid = t.test(args)
            if valid:
                print('not requesting', valid)
                return valid
            else:
                print('requesting...')
                res = fun(args[0])
                t.update(args[0], res)
                return res

        return inner

    return func
