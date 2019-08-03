# coding: utf-8
# pyweathercn - meizu.py
# 2019/2/26 15:37

__author__ = 'Benny <benny@bennythink.com>'

import requests

from pyweathercn.utils import cache
from pyweathercn.constant import CITY, CODE


@cache(timeout=10800)
def make_json(city):
    city_code = CITY.get(city)
    # city not found
    if city_code is None:
        return {"code": 400001, "message": CODE[400001], "error": CODE[400001]}

    url = 'http://aider.meizu.com/app/weather/listWeather?cityIds={}'.format(city_code)
    sample = requests.get(url).json()
    tip, forecast, result = '', [], {}

    for each in sample['value'][0]['indexes']:
        tip = tip + '{}：{}\n'.format(each["name"], each["content"])

    aqi = "{} {}".format(sample['value'][0]['pm25']['aqi'], sample['value'][0]['pm25']['quality'])

    temp = sample['value'][0]['realtime']['temp']

    for item in sample['value'][0]['weathers']:
        date = "{} {}".format(item['date'], item['week'])
        _type = item['weather']
        temp = '{}/{}℃'.format(item["temp_day_c"], item["temp_night_c"])
        sun_rise = item["sun_rise_time"]
        sun_down = item["sun_down_time"]
        forecast.append(dict(date=date, type=_type, temp=temp, sun_rise=sun_rise, sun_down=sun_down, wind=''))

    result['city'] = sample['value'][0]['city']
    result['aqi'] = aqi
    result['tip'] = tip
    result['temp'] = temp
    result['forecast'] = forecast
    result['wind'] = "{} {}".format(sample['value'][0]['realtime']['wD'], sample['value'][0]['realtime']['wS'])

    return result


if __name__ == '__main__':
    r = make_json('南京')
    print(r)
