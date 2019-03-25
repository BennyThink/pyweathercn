#!/usr/bin/python
# coding:utf-8

# pyweathercn - craw.py
# 2018/5/22 16:31
# get forecast from weather.com.cn

__author__ = 'Benny <benny@bennythink.com>'

import json
import time

import requests
from bs4 import BeautifulSoup

from pyweathercn.constant import CITY, CODE
from pyweathercn.utils import cache


def today_tip(soup):
    s = ''
    tips = soup.find('li', class_='li1')
    s += tips.em.string + tips.span.string + tips.p.string
    tips = soup.find('li', class_='li3 hot')
    s += tips.em.string + tips.span.string + tips.p.string
    return s


def js_hour_aqi(soup):
    script = soup.find_all('script')
    js = script[5].string
    od = json.loads(js[js.index('=') + 2:js.index(';')])
    aqi = [i['od28'] for i in od['od']['od2'] if i['od21'] == time.strftime('%H', time.localtime(3))][0]
    return aqi


def js_hour_temp(soup):
    """
    get hour temperature extract from JavaScript object and dumps it to dict.
    :param soup: beautiful soup object
    :return:temperature
    """
    script = soup.find_all('script')
    js = script[3].string
    od = json.loads(js[js.index('=') + 1:])

    hour = int(time.strftime('%H', time.localtime()))
    if 1 <= hour <= 3:
        hour = '02'
    elif 4 <= hour <= 6:
        hour = '05'
    elif 7 <= hour <= 9:
        hour = '08'
    elif 10 <= hour <= 13:
        hour = '11'
    elif 13 <= hour <= 15:
        hour = '14'
    elif 16 <= hour <= 18:
        hour = '17'
    elif 19 <= hour <= 21:
        hour = '20'
    elif 22 <= hour or hour <= 0:
        hour = '23'

    current_temp = [i.split(',')[3].split('℃')[0] for i in od['1d'] if hour + '时' in i][0]
    return current_temp


def seven_day(soup):
    ul_res = soup.find_all('ul', class_='t clearfix')

    date = wea = tem = win = None
    for ul in ul_res:
        date = ul.find_all('h1')
        wea = ul.find_all('p', class_="wea")
        tem = ul.find_all('p', class_="tem")
        win = ul.find_all('p', class_="win")

    date_list = [data.string for data in date]
    wea_list = [w['title'] for w in wea]
    tem_list = []
    for t in tem:
        if t.span is None:
            tem_list.append(t.i.string)
        else:
            tem_list.append(t.span.string + '/' + t.i.string)

    win_list = [w.em.span['title'] + ' ' + w.i.string for w in win]

    a = [{'date': date_list[i], 'type': wea_list[i], 'temp': tem_list[i], 'wind': win_list[i]} for i in
         range(len(date_list))]
    return a


def convert_city(name):
    return CITY.get(name)


@cache(timeout=10800)
def make_json(city):
    """
    make final request json
    :param city: city name
    :return: result dict
    """
    city_code = convert_city(city)
    # city not found
    if city_code is None:
        return {"code": 400001, "message": CODE[400001], "error": CODE[400001]}

    try:
        url = 'http://www.weather.com.cn/weather/%s.shtml'
        response = requests.get(url % city_code)
        if response.status_code != 200:
            return {"code": 500001, "message": CODE[500001], "error": "Not receiving 200 from weather.com.cn"}

        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, 'html.parser')

        sample = {"city": city, "aqi": js_hour_aqi(soup), "tip": today_tip(soup), "temp": js_hour_temp(soup),
                  "forecast": seven_day(soup)}
        response.close()
        return sample
    except Exception as e:
        sample = {"code": 500002, "message": CODE[500002], "error": str(e)}
        return sample


if __name__ == '__main__':
    print(make_json('深圳'))
