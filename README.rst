pyweathercn:
============
.. image:: https://travis-ci.org/BennyThink/pyweathercn.svg?branch=master
    :target: https://travis-ci.org/BennyThink/pyweathercn
.. image:: https://badge.fury.io/py/pyweathercn.svg
    :target: https://badge.fury.io/py/pyweathercn

An weather forecast library from www.weather.com.cn

Installation
------------

To install this package, simply use pip: ``$ pip3 install pyweathercn``.

There's no plan to support Python 2.

Example
--------

Python Console example:
******************************

.. code:: python

       >>> import pyweathercn
       >>> pyweathercn.Weather('重庆').temp()
       '重庆：20'
       >>> w = pyweathercn.Weather('北京')
       >>> w.data
       {'city': '北京', 'aqi': '73', 'tip': '紫外线指数中等涂擦SPF大于15、PA+防晒护肤品。穿衣指数较舒适建议穿薄外套或牛仔裤等服装。', 'temp': '11', 'forecast': [{'date': '17日（今天）', 'type': '晴', 'temp': '4℃', 'wind': '无持续风向 <3级'}, {'date': '18日（明天）', 'type': '晴', 'temp': '18℃/5℃', 'wind': '南风 <3级'}, {'date': '19日（后天）', 'type': '多云', 'temp': '18℃/6℃', 'wind': '西南风 <3级'}, {'date': '20日（周六）', 'type': '多云', 'temp': '18℃/7℃', 'wind': '南风 <3级'}, {'date': '21日（周日）', 'type': '多云', 'temp': '18℃/8℃', 'wind': '南风 <3级'}, {'date': '22日（周一）', 'type': '多云转晴', 'temp': '19℃/7℃', 'wind': '南风 <3级'}, {'date': '23日（周二）', 'type': '晴', 'temp': '19℃/5℃', 'wind': '西风 <3级'}]}
       >>> w.today()
       '北京：23日（今天）晴15℃西南风 3-4级'
       >>> w.tomorrow(True)
       {'date': '24日（明天）', 'type': '晴', 'temp': '31℃/17℃', 'wind': '南风 3-4级'}
       >>> w.tip()
       '北京温馨提示：紫外线指数很强涂擦SPF20以上，PA++护肤品，避强光。穿衣指数热适合穿T恤、短薄外套等夏季服装。'
       >>> w.forecast(False,5)
       '北京：28日（周一）多云25℃/15℃东北风 <3级'

Run as a server:
******************************
In order for better performance, please install Redis.

.. code:: python

       import pyweathercn
       # running on http://127.0.0.1:8888
       pyweathercn.server(host='127.0.0.1')
       # running on http://0.0.0.0:3333
       pyweathercn.server(3333)
       # support ssl: https://www.example.com:8888
       # if you fail to listen on www.example.com, you may try 0.0.0.0 instead.
       pyweathercn.server('8888', 'www.example.com', ssl_options={
           "certfile": "fullchain.pem",
           "keyfile": "privkey.pem"})

To access REST API, you may try GET parameter, POST form-data/url-encoded form-data and POST JSON.

Mandatory parameter is city, optional parameter is day.

GET: ``http://127.0.0.1:8888/weather?city=上海&day=2``

POST:``http://127.0.0.1:8888/weather`` with form/json key-value:{"city","深圳"}


Run as a server(with API authentication):
*********************************************

.. code:: python

       import pyweathercn
       # running on http://0.0.0.0:3333
       pyweathercn.server(auth='/path/to/database.sqlite')

Please refer to ``sample.sqlite`` for database format. In this sample:

* times: total times for access this API
* restrict: set to 0 avoid time limit
* key: no more than 32 characters.

You only need to add a parameter called ``key`` for your request.

About cURL
----------
If you're using cURL on Windows(such as ``git bash``, ``MinGW``), you may receive an HTTP 400.

This is because cURL will try to encode query parameters by GBK instead of UTF-8.
This might be an implementation bug on Windows, I'm looking on it.

For now the best thing you should do is use url-encode for all your city name.

TODO
-----
- add server deployment: systemd and docker
- cURL compatibility

Design
-------
`RESETful API Specification <https://github.com/godruoyi/restful-api-specification>`_

License
-------
MIT
