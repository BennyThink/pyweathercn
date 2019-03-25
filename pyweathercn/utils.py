#!/usr/bin/python
# coding: utf-8

# pyweathercn - utils.py
# 2018/8/18 15:12
# decorator utilities, for API Key authentication and so on

__author__ = "Benny <benny@bennythink.com>"

import logging
import json
import socket
import sqlite3

import redis

from pyweathercn.constant import CODE

DB = ":memory:"
logging.basicConfig(level=logging.INFO)


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
                v = (False, {"code": 429001, "message": CODE[429001], "error": CODE[429001]})
            else:
                # invalid key provided
                v = (False, {"code": 401001, "message": CODE[401001], "error": CODE[401001]})

        return v

    @staticmethod
    def get_key(s):
        # get parameter, compatibility with json
        if s.request.headers.get('Content-Type') == 'application/json' and s.request.body:
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
        self.__timeout = timeout
        self.r = redis.Redis(decode_responses=True)

    def retrieve(self, city):
        result = self.r.get(city)
        if result:
            return json.loads(self.r.get(city))

    def update(self, city, weather):
        if weather.get('code') is None:
            self.r.set(city, json.dumps(weather, ensure_ascii=False), ex=self.__timeout)

    @staticmethod
    def check_redis():
        try:
            s = socket.socket()
            s.connect(("127.0.0.1", 6379))
            s.close()
            return True
        except ConnectionRefusedError:
            return False


def cache(timeout):
    def func(fun):
        def inner(*args):
            if TestCache.check_redis():
                t = TestCache(timeout)
                valid = t.retrieve(args[0])
                if valid:
                    logging.info('Retrieving data from redis')
                    return valid
                else:
                    logging.info('Cache expired. Re-requesting now...')
                    res = fun(args[0])
                    t.update(args[0], res)
                    return res
            else:
                logging.warning('Please install Redis for better performance!')
                res = fun(args[0])
                return res

        return inner

    return func
