# coding: utf-8
# pyweathercn - meizu.py
# 2019/2/26 15:37

__author__ = 'Benny <benny@bennythink.com>'

import requests
from pyweathercn.utils import cache
from pyweathercn.constant import CITY

sample = {
    "code": "200",
    "message": "",
    "redirect": "",
    "value": [
        {
            "alarms": [],
            "city": "大连",
            "cityid": 101070201,
            "indexes": [
                {
                    "abbreviation": "pp",
                    "alias": "",
                    "content": "天气寒冷，多补水，选用滋润保湿型化妆品，使用润唇膏。",
                    "level": "保湿",
                    "name": "化妆指数"
                },
                {
                    "abbreviation": "yd",
                    "alias": "",
                    "content": "受到大风天气的影响，不宜在户外运动。",
                    "level": "不适宜",
                    "name": "运动指数"
                },
                {
                    "abbreviation": "gm",
                    "alias": "",
                    "content": "感冒较易发生，干净整洁的环境和清新流通的空气都有利于降低感冒的几率，体质较弱的童鞋们要特别加强自我保护。",
                    "level": "较易发",
                    "name": "感冒指数"
                },
                {
                    "abbreviation": "xc",
                    "alias": "",
                    "content": "洗车后，可至少保持4天车辆清洁，非常适宜洗车。",
                    "level": "非常适宜",
                    "name": "洗车指数"
                },
                {
                    "abbreviation": "ct",
                    "alias": "",
                    "content": "天气较热，衣物精干简洁，室内酌情添加空调衫。",
                    "level": "热",
                    "name": "穿衣指数"
                },
                {
                    "abbreviation": "uv",
                    "alias": "",
                    "content": "辐射较弱，涂擦SPF12-15、PA+护肤品。",
                    "level": "弱",
                    "name": "紫外线强度指数"
                }
            ],
            "pm25": {
                "advice": "0",
                "aqi": "43",
                "citycount": 679,
                "cityrank": 72,
                "co": "8",
                "color": "0",
                "level": "0",
                "no2": "22",
                "o3": "14",
                "pm10": "43",
                "pm25": "30",
                "quality": "优",
                "so2": "7",
                "timestamp": "",
                "upDateTime": "2019-02-26 15:00:00"
            },
            "provinceName": "辽宁省",
            "realtime": {
                "img": "0",
                "sD": "29",
                "sendibleTemp": "7",
                "temp": "7",
                "time": "2019-02-26 16:25:08",
                "wD": "南风",
                "wS": "1级",
                "weather": "晴",
                "ziwaixian": "N/A"
            },
            "weatherDetailsInfo": {
                "publishTime": "2019-02-26 16:00:00",
                "weather3HoursDetailsInfos": [
                    {
                        "endTime": "2019-02-26 20:00:00",
                        "highestTemperature": "5",
                        "img": "2",
                        "isRainFall": "",
                        "lowerestTemperature": "5",
                        "precipitation": "0",
                        "startTime": "2019-02-26 17:00:00",
                        "wd": "",
                        "weather": "阴",
                        "ws": ""
                    },
                    {
                        "endTime": "2019-02-26 23:00:00",
                        "highestTemperature": "1",
                        "img": "2",
                        "isRainFall": "",
                        "lowerestTemperature": "1",
                        "precipitation": "0",
                        "startTime": "2019-02-26 20:00:00",
                        "wd": "",
                        "weather": "阴",
                        "ws": ""
                    },
                    {
                        "endTime": "2019-02-27 02:00:00",
                        "highestTemperature": "0",
                        "img": "2",
                        "isRainFall": "",
                        "lowerestTemperature": "0",
                        "precipitation": "0",
                        "startTime": "2019-02-26 23:00:00",
                        "wd": "",
                        "weather": "阴",
                        "ws": ""
                    },
                    {
                        "endTime": "2019-02-27 05:00:00",
                        "highestTemperature": "1",
                        "img": "2",
                        "isRainFall": "",
                        "lowerestTemperature": "1",
                        "precipitation": "0",
                        "startTime": "2019-02-27 02:00:00",
                        "wd": "",
                        "weather": "阴",
                        "ws": ""
                    },
                    {
                        "endTime": "2019-02-27 08:00:00",
                        "highestTemperature": "1",
                        "img": "2",
                        "isRainFall": "",
                        "lowerestTemperature": "1",
                        "precipitation": "0",
                        "startTime": "2019-02-27 05:00:00",
                        "wd": "",
                        "weather": "阴",
                        "ws": ""
                    },
                    {
                        "endTime": "2019-02-27 11:00:00",
                        "highestTemperature": "3",
                        "img": "2",
                        "isRainFall": "",
                        "lowerestTemperature": "3",
                        "precipitation": "0",
                        "startTime": "2019-02-27 08:00:00",
                        "wd": "",
                        "weather": "阴",
                        "ws": ""
                    },
                    {
                        "endTime": "2019-02-27 14:00:00",
                        "highestTemperature": "7",
                        "img": "2",
                        "isRainFall": "",
                        "lowerestTemperature": "7",
                        "precipitation": "0",
                        "startTime": "2019-02-27 11:00:00",
                        "wd": "",
                        "weather": "阴",
                        "ws": ""
                    }
                ]
            },
            "weathers": [
                {
                    "date": "2019-02-26",
                    "img": "0",
                    "sun_down_time": "17:42",
                    "sun_rise_time": "06:31",
                    "temp_day_c": "8",
                    "temp_day_f": "46.4",
                    "temp_night_c": "0",
                    "temp_night_f": "32.0",
                    "wd": "",
                    "weather": "晴",
                    "week": "星期二",
                    "ws": ""
                },
                {
                    "date": "2019-02-27",
                    "img": "1",
                    "sun_down_time": "17:42",
                    "sun_rise_time": "06:31",
                    "temp_day_c": "8",
                    "temp_day_f": "46.4",
                    "temp_night_c": "1",
                    "temp_night_f": "33.8",
                    "wd": "",
                    "weather": "多云",
                    "week": "星期三",
                    "ws": ""
                },
                {
                    "date": "2019-02-28",
                    "img": "0",
                    "sun_down_time": "17:42",
                    "sun_rise_time": "06:31",
                    "temp_day_c": "9",
                    "temp_day_f": "48.2",
                    "temp_night_c": "2",
                    "temp_night_f": "35.6",
                    "wd": "",
                    "weather": "晴",
                    "week": "星期四",
                    "ws": ""
                },
                {
                    "date": "2019-03-01",
                    "img": "0",
                    "sun_down_time": "17:42",
                    "sun_rise_time": "06:31",
                    "temp_day_c": "9",
                    "temp_day_f": "48.2",
                    "temp_night_c": "1",
                    "temp_night_f": "33.8",
                    "wd": "",
                    "weather": "晴",
                    "week": "星期五",
                    "ws": ""
                },
                {
                    "date": "2019-03-02",
                    "img": "1",
                    "sun_down_time": "17:42",
                    "sun_rise_time": "06:31",
                    "temp_day_c": "7",
                    "temp_day_f": "44.6",
                    "temp_night_c": "2",
                    "temp_night_f": "35.6",
                    "wd": "",
                    "weather": "多云",
                    "week": "星期六",
                    "ws": ""
                },
                {
                    "date": "2019-03-03",
                    "img": "0",
                    "sun_down_time": "17:42",
                    "sun_rise_time": "06:31",
                    "temp_day_c": "8",
                    "temp_day_f": "46.4",
                    "temp_night_c": "1",
                    "temp_night_f": "33.8",
                    "wd": "",
                    "weather": "晴",
                    "week": "星期日",
                    "ws": ""
                },
                {
                    "date": "2019-02-25",
                    "img": "0",
                    "sun_down_time": "17:42",
                    "sun_rise_time": "06:31",
                    "temp_day_c": "6",
                    "temp_day_f": "42.8",
                    "temp_night_c": "0",
                    "temp_night_f": "32.0",
                    "wd": "",
                    "weather": "晴",
                    "week": "星期一",
                    "ws": ""
                }
            ]
        }
    ]
}


@cache(timeout=10800)
def make_json(city):
    pass


make_json('大连')