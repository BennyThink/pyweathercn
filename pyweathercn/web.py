#!/usr/bin/python
# coding:utf-8

# pyweathercn - web.py
# 2018/5/22 16:32
# For running up tornado

__author__ = 'Benny <benny@bennythink.com>'

import json
import socket
from platform import uname

from concurrent.futures import ThreadPoolExecutor
from tornado import web, ioloop, httpserver, gen
from tornado.concurrent import run_on_executor
from pyweathercn.utils import api
from pyweathercn.constant import CODE, BANNER, HTTP


class BaseHandler(web.RequestHandler):
    def data_received(self, chunk):
        pass


class IndexHandler(BaseHandler):

    def get(self):
        help_msg = '''Welcome to pyweathercn!
        There are two ways to interact with this RESTAPI.
        The key parameter is city, and an optional parameter day.<br>
        The first one is GET method, invoke:
        <code>127.0.0.1:8888/weather?city=上海</code> - get full details
        <code>127.0.0.1:8888/weather?city=上海&day=2</code> - get 2 days details
        The second one is POST method, invoke <code>127.0.0.1:8888/weather</code>
         with url-encoded form as above. Post JSON is also supported.
        '''.replace('\n', '<br>')

        base = f'''<!DOCTYPE html><html><head><title>Welcome to pyweathercn!</title></head>
                <body><pre>{BANNER}</pre><br>{help_msg}</body></html>'''
        self.write(base)

    def post(self):
        self.get()


def compatible_get_arguments(self):
    from tornado.web import HTTPError
    try:
        c = self.get_argument('city', None)
    except HTTPError:
        c = self.request.query_arguments['city'][0].decode('gbk')
    return c


class WeatherHandler(BaseHandler):
    executor = ThreadPoolExecutor(max_workers=20)
    PROVIDER = None

    @run_on_executor
    def run_request(self):
        """
        sign and return
        :return: hex and raw request in XML
        """
        # get parameter, compatibility with json
        if WeatherHandler.PROVIDER == 'meizu':
            from pyweathercn.meizu import make_json
        else:
            from pyweathercn.craw import make_json

        if self.request.headers.get('Content-Type') == 'application/json' and self.request.body:
            data = json.loads(self.request.body)
            city = data.get('city')
            day = data.get('day')
        else:
            city = compatible_get_arguments(self)
            day = self.get_argument('day', None)
        # mandatory param missing
        if city is None:
            self.set_status(HTTP.get(400002))
            response = {"code": 400002, "message": CODE[400002], "error": CODE[400002]}
        # day, return specified day.
        elif day:
            data = make_json(city)
            try:
                response = data['forecast'][int(day)]
            except IndexError as e:
                response = {"code": 400003, "message": CODE[400003], "error": str(e)}
            except KeyError as e:
                response = {"code": 400001, "message": CODE[400001], "error": str(e)}

        # return whole json.
        else:
            response = make_json(city)
        # set http code and response
        self.set_status(HTTP.get(response.get('code'), 418))
        return response

    @api
    @gen.coroutine
    def get(self):
        res = yield self.run_request()
        self.write(res)

    @api
    @gen.coroutine
    def post(self):
        res = yield self.run_request()
        self.write(res)


class NotFoundHandler(BaseHandler):
    def prepare(self):  # for all methods
        self.set_status(HTTP[404001])
        response = {"code": 404001, "message": CODE[404001], "error": CODE[404001]}
        self.write(response)

    def get(self):
        pass

    def post(self):
        pass


def get_host_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('8.8.8.8', 80))
    ip = s.getsockname()[0]
    s.close()
    return ip


class RunServer:
    handlers = [(r'/weather', WeatherHandler), (r'/', IndexHandler)]
    application = web.Application(handlers, default_handler_class=NotFoundHandler)

    @staticmethod
    def run_server(port=8888, host='0.0.0.0', **kwargs):
        tornado_server = httpserver.HTTPServer(RunServer.application, **kwargs)
        tornado_server.bind(port, host)

        if uname()[0] == 'Windows':
            tornado_server.start()
        else:
            tornado_server.start(None)

        try:
            print(BANNER)
            print(f'Server is running on http://{get_host_ip()}:{port}')
            print(f'Running server with {WeatherHandler.PROVIDER or "weather.com.cn"}')
            ioloop.IOLoop.instance().current().start()
        except KeyboardInterrupt:
            ioloop.IOLoop.instance().stop()
            print('"Ctrl+C" received, exiting.\n')


if __name__ == "__main__":
    # import pyweathercn.utils
    # pyweathercn.utils.DB = r'C:\Users\Benny\PycharmProjects\pyweathercn\sample.sqlite'
    WeatherHandler.PROVIDER = 'meizu'
    RunServer.run_server()
