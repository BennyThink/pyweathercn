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
    Usage:
    1. chain call:`pyweathercn.Weather('重庆').temp()`
    2. instance mode: ```  w = pyweathercn.Weather('北京')
                            w.data```
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
        """
        forecast in assigning days. 0 stands for today, 1 for tomorrow. the number could be no larger than 6.
        :param raw: raw json
        :param day: day option. Default is 0 which will return today's weather information.
        :return: json response
        """
        if raw and self.data['status'] == 0:
            return self.data['data']['forecast'][day]
        elif self.data['status'] == 0:
            return self.data['data']['city'] + '：' + self.__make_str__(self.data['data']['forecast'][day])
        else:
            return self.data['desc']

    def __make__(self, raw, _type, text):
        """
        make specified json
        :param raw: raw json or not
        :param _type: aqi, temp or tip?
        :param text: default tooltip
        :return: json response.
        """
        if raw and self.data['status'] == 0:
            return self.data['data'][_type]

        elif self.data['status'] == 0:
            return self.data['data']['city'] + text + "：" + self.data['data'][_type]
        else:
            return self.data['desc']

    def __return_result__(self, raw, index):
        """
        today, tomorrow, two_days, three_days.
        :param raw: set True to return raw json, otherwise it shall return plain string.
        :param index: index for forecast function.
        :return: response.
        """
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
    """
    run RESTAPI server.
    :param port: the port to listen on. Default is 8888
    :param host: the host to listen on. Default is localhost.
    :param kwargs: any keyword argument support by tornado. example for SSL:
    ```ssl_options={
        "certfile": "fullchain.pem",
        "keyfile": "privkey.pem"}
    ```
    :return: None
    """
    pyweathercn.helper.run_server(port, host, **kwargs)
