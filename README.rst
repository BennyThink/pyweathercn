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
       {'data': {'city': '北京', 'aqi': '159', 'tip': '紫外线指数很强涂擦SPF20以上，PA++护肤品，避强光。穿衣指数热适合穿T恤、短薄外套等夏季服装。', 'temp': '20', 'forecast': [{'date': '23日（今天）', 'type': '晴', 'temp': '15℃', 'wind': '西南风 3-4级'}, {'date': '24日（明天）', 'type': '晴', 'temp': '31℃/17℃', 'wind': '南风 3-4级'}, {'date': '25日（后天）', 'type': '晴转多云', 'temp': '31℃/19℃', 'wind': '西南风 <3级'}, {'date': '26日（周六）', 'type': '阴转多云', 'temp': '30℃/16℃', 'wind': '西风 <3级'}, {'date': '27日（周日）', 'type': '多云', 'temp': '29℃/15℃', 'wind': '南风 <3级'}, {'date': '28日（周一）', 'type': '多云', 'temp': '25℃/15℃', 'wind': '东北风 <3级'}, {'date': '29日（周二）', 'type': '晴', 'temp': '29℃/15℃', 'wind': '西南风 <3级'}]}, 'status': 0, 'message': 'success'}
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

TODO
-----
- add server deployment: normal systemd and docker


License
-------
MIT
