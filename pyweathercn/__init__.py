#!/usr/bin/python
# coding:utf-8

# pyweathercn - __init__.py
# 2018/5/23 16:32
# 

__author__ = 'Benny <benny@bennythink.com>'

import pyweathercn.helper


class Weather:
    """
    Weather broadcast class.
    """

    def __init__(self, city_name):

        self.data = pyweathercn.helper.make_json(city_name)

    def __del__(self):
        del self.data

    def today(self, raw=False):
        """
        return today weather
        :param raw: return raw json
        :return: json or string.
        """
        return self.__return_result__(raw, 0)

    def tomorrow(self, raw=False):
        return self.__return_result__(raw, 1)

    def two_days(self, raw=False):
        return self.__return_result__(raw, 2)

    def three_days(self, raw=False):
        return self.__return_result__(raw, 3)

    def aqi(self, raw=False):
        return self.__make__(raw, 'aqi', 'AQI')

    def temp(self, raw=False):
        return self.__make__(raw, 'temp', '')

    def tip(self, raw=False):
        return self.__make__(raw, 'tip', '温馨提示')

    def forecast(self, raw=False, day=0):
        if raw and self.data['status'] == 0:
            return self.data['data']['forecast'][day]
        elif self.data['status'] == 0:
            return self.data['data']['city'] + '：' + self.__make_str__(self.data['data']['forecast'][day])
        else:
            return self.data['desc']

    def __make__(self, raw, _type, text):
        if raw and self.data['status'] == 0:
            return self.data['data'][_type]

        elif self.data['status'] == 0:
            return self.data['data']['city'] + text + "：" + self.data['data'][_type]
        else:
            return self.data['desc']

    def __return_result__(self, raw, index):
        if raw and self.data['status'] == 0:
            return self.data['data']['forecast'][index]
        elif self.data['status'] == 0:
            return self.data['data']['city'] + '：' + self.__make_str__(self.data['data']['forecast'][index])
        else:
            return self.data['desc']

    @staticmethod
    def __make_str__(dic):
        s = ''
        for i in dic:
            s = s + dic[i]
        return s


def server(port=8888, host="127.0.0.1", **kwargs):
    pyweathercn.helper.run_server(port, host, **kwargs)
