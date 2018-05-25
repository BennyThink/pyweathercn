#!/usr/bin/python
# coding:utf-8

# pyweathercn - test_weather.py
# 2018/5/25 20:26
# 

__author__ = 'Benny <benny@bennythink.com>'

import sys
import unittest

sys.path.append('.')

import pyweathercn
from tests.deco import logger


class TestWeather(unittest.TestCase):
    w = pyweathercn.Weather('深圳')

    @logger
    def test_today(self):
        self.assertIn('℃', self.w.today())
        self.assertIsInstance(self.w.today(True), dict)

    @logger
    def test_tomorrow(self):
        self.assertIn('℃', self.w.tomorrow())
        self.assertIsInstance(self.w.tomorrow(True), dict)

    @logger
    def test_two_days(self):
        self.assertIn('℃', self.w.two_days())
        self.assertIsInstance(self.w.two_days(True), dict)

    @logger
    def test_three_days(self):
        self.assertIn('℃', self.w.three_days())
        self.assertIsInstance(self.w.three_days(True), dict)

    @logger
    def test_forecast(self):
        self.assertIn('℃', self.w.forecast())
        self.assertIsInstance(self.w.forecast(True), dict)

    @logger
    def test_temp(self):
        self.assertNotEqual(0, len(self.w.temp().split('：')[1]))
        self.assertNotEqual(0, len(self.w.temp(True)))

    @logger
    def test_tip(self):
        self.assertNotEqual(0, len(self.w.tip()))

    @logger
    def test_aqi(self):
        self.assertNotEqual(0, len(self.w.aqi().split('：')[1]))
        self.assertNotEqual(0, len(self.w.aqi(True)))


if __name__ == '__main__':
    unittest.main()
