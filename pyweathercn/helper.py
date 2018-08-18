#!/usr/bin/python
# coding:utf-8

# pyweathercn - helper.py
# 2018/5/22 16:32
# 

__author__ = 'Benny <benny@bennythink.com>'

import json

import tornado.ioloop
import tornado.web

from pyweathercn.craw import make_json


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.set_header("Content-Type", "application/json")
        self.write(self.process(self))

    def post(self):
        self.set_header("Content-Type", "application/json")
        self.write(self.process(self))

    @staticmethod
    def process(self):
        # get parameter

        city = self.get_argument('city', None)
        day = self.get_argument('day', None)

        # mandatory param missing
        if city is None:
            return make_json(4)
        # day, return specified day.
        elif day:
            data = make_json(city)
            try:
                sp = data['data']['forecast'][int(day)]
            except IndexError:
                sp = {"status": 3, "message": 'day out of range'}
            return json.dumps(sp)
        # return whole json.
        else:
            return json.dumps(make_json(city))


def make_app():
    return tornado.web.Application([
        (r"/weather", MainHandler),
    ])


def run_server(port, host, **kwargs):
    app = make_app()
    app.listen(port, host, **kwargs)
    print('%s running on %s' % (host, port))
    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    run_server('8888', 'api.serversan.date', ssl_options={
        "certfile": "fullchain.pem",
        "keyfile": "privkey.pem"})
