#!/usr/bin/python
# coding:utf-8

# pyweathercn - __init__.py
# 2018/5/23 16:32
# 

__author__ = 'Benny <benny@bennythink.com>'

import os

import pyweathercn.web
import pyweathercn.utils

from pyweathercn.craw import make_json


class Weather:
    """
    Weather broadcast class.
    Usage:
    1. chain call:`pyweathercn.Weather('重庆').temp()`
    2. instance mode: ```  w = pyweathercn.Weather('北京')
                            w.data```
    """

    def __init__(self, city_name):
        self.data = make_json(city_name)

    def __del__(self):
        del self.data

    def today(self, raw=False):
        """
        return today weather
        :param raw: return raw json
        :return: json or string.
        """
        return self.__return_result(raw, 0)

    def tomorrow(self, raw=False):
        return self.__return_result(raw, 1)

    def two_days(self, raw=False):
        return self.__return_result(raw, 2)

    def three_days(self, raw=False):
        return self.__return_result(raw, 3)

    def aqi(self, raw=False):
        return self.__make(raw, 'aqi', 'AQI')

    def temp(self, raw=False):
        return self.__make(raw, 'temp', '')

    def tip(self, raw=False):
        return self.__make(raw, 'tip', '温馨提示')

    def forecast(self, raw=False, day=0):
        """
        forecast in assigning days. 0 stands for today, 1 for tomorrow. the number could be no larger than 6.
        :param raw: raw json
        :param day: day option. Default is 0 which will return today's weather information.
        :return: json response
        """
        if raw and self.data.get('code') is None:
            return self.data['forecast'][day]
        elif self.data.get('code') is None:
            return self.data['city'] + '：' + self.__make_str(self.data['forecast'][day])
        else:
            return self.data['message']

    def __make(self, raw, _type, text):
        """
        make specified json
        :param raw: raw json or not
        :param _type: aqi, temp or tip?
        :param text: default tooltip
        :return: json response.
        """
        if raw and self.data.get('code') is None:
            return self.data[_type]

        elif self.data.get('code') is None:
            return self.data['city'] + text + "：" + self.data[_type]
        else:
            return self.data['message']

    def __return_result(self, raw, index):
        """
        today, tomorrow, two_days, three_days.
        :param raw: set True to return raw json, otherwise it shall return plain string.
        :param index: index for forecast function.
        :return: response.
        """
        if raw and self.data.get('code') is None:
            return self.data['forecast'][index]
        elif self.data.get('code') is None:
            return self.data['city'] + '：' + self.__make_str(self.data['forecast'][index])
        else:
            return self.data['message']

    @staticmethod
    def __make_str(dic):
        s = ''
        for i in dic:
            s = s + dic[i]
        return s


def server(port=8888, host="0.0.0.0", auth=None, provider='meizu', **kwargs):
    """
    run RESTAPI server.
    :param port: the port to listen on. Default is 8888
    :param host: the host to listen on. Default is localhost.
    :param auth: API authentication database path
    :param provider: which provider to use, meizu or weathercn
    :param kwargs: any keyword argument support by tornado. example for SSL:
    ```ssl_options={
        "certfile": "fullchain.pem",
        "keyfile": "privkey.pem"}
    ```
    :return: None
    """
    if auth is not None and not os.path.isfile(auth):
        raise FileNotFoundError('Database file not exists!')
    else:
        pyweathercn.web.WeatherHandler.PROVIDER = provider
        pyweathercn.utils.DB = auth
        pyweathercn.web.RunServer.run_server(port, host, **kwargs)
