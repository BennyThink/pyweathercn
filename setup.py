#!/usr/bin/python
# coding:utf-8

# pyweathercn - setup.py
# 2018/5/23 16:07
# 

__author__ = 'Benny <benny@bennythink.com>'

from distutils.core import setup

setup(
    name='pyweathercn',
    version='0.0.3',
    author='BennyThink',
    author_email='benny@bennythink.com',
    packages=['pyweathercn'],
    url='https://github.com/BennyThink/pyweathercn',
    license='LICENSE.txt',
    description='pyweathercn forecast',
    long_description=open('README', encoding='utf-8').read(),
    install_requires=[
        "flask",
        "beautifulsoup4",
        "requests"
    ],
)
