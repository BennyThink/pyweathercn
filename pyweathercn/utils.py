#!/usr/bin/python
# coding: utf-8

# pyweathercn - utils.py
# 2018/8/18 15:12
# decorator utilities, for API Key authentication and so on

__author__ = "Benny <benny@bennythink.com>"

import sqlite3
import json

from pyweathercn.constant import CODE

DB = ":memory:"


def auth(k):
    print(123, DB)
    if DB == ":memory:" or DB is None:
        # disable auth
        return True, None
    elif k is None:
        # key required
        return False, {"status": 6, "message": CODE.get(6)}
    else:
        con = sqlite3.connect(DB)
        cur = con.cursor()
        cur.execute('SELECT times,restrict FROM auth WHERE key=?', (k,))
        data = cur.fetchall()

        if data and data[0][1] == 0:
            # unlimited user
            v = (True, None)
        elif data and data[0][0] >= 1:
            # valid, limited user. we need to decrease.
            cur.execute('UPDATE auth SET times=? WHERE key=?', (data[0][0] - 1, k))
            con.commit()
            v = (True, None)
        elif data and data[0][0] <= 0:
            # exceed
            v = (False, {"status": 7, "message": CODE.get(7)})
        else:
            # invalid key provided
            v = (False, {"status": 6, "message": CODE.get(6)})

        con.close()
        return v


def get_key(self):
    # get parameter, compatibility with json
    if self.request.headers.get('Content-Type') == 'application/json':
        data = json.loads(self.request.body)
        key = data.get('key')
    else:
        key = self.get_argument('key', None)

    return key


def require_api(fun):
    def wrapper(self):
        k, msg = auth(get_key(self))
        if not k:
            self.write(msg)
        else:
            res = fun(self)
            return res

    return wrapper
