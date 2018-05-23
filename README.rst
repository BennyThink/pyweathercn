py weather cn
=========================


Hey

.. code-block:: python

    >>> import pyweathercn
    >>> pyweathercn.Weather('重庆').temp()
    '重庆：20'
    >>> w = pyweathercn.Weather('北京')
    >>> w.data
    {'data': {'city': '北京', 'aqi': '159', 'tip': '紫外线指数很强涂擦SPF20以上，PA++护肤品，避强光。穿衣指数热适合穿T恤、短薄外套等夏季服装。', 'temp': '20', 'forecast': [{'date': '23日（今天）', 'type': '晴', 'temp': '15℃', 'wind': '西南风 3-4级'}, {'date': '24日（明天）', 'type': '晴', 'temp': '31℃/17℃', 'wind': '南风 3-4级'}, {'date': '25日（后天）', 'type': '晴转多云', 'temp': '31℃/19℃', 'wind': '西南风 <3级'}, {'date': '26日（周六）', 'type': '阴转多云', 'temp': '30℃/16℃', 'wind': '西风 <3级'}, {'date': '27日（周日）', 'type': '多云', 'temp': '29℃/15℃', 'wind': '南风 <3级'}, {'date': '28日（周一）', 'type': '多云', 'temp': '25℃/15℃', 'wind': '东北风 <3级'}, {'date': '29日（周二）', 'type': '晴', 'temp': '29℃/15℃', 'wind': '西南风 <3级'}]}, 'status': 0, 'desc': 'success'}
    >>> w.today()
    '北京：23日（今天）晴15℃西南风 3-4级'
    >>> w.tomorrow(True)
    {'date': '24日（明天）', 'type': '晴', 'temp': '31℃/17℃', 'wind': '南风 3-4级'}
    >>> w.tip()
    '北京温馨提示：紫外线指数很强涂擦SPF20以上，PA++护肤品，避强光。穿衣指数热适合穿T恤、短薄外套等夏季服装。'
    >>> w.forecast(False,5)
    '北京：28日（周一）多云25℃/15℃东北风 <3级'


Installation
------------

To install this package, simply use `pipenv <http://pipenv.org/>`_ (or pip, of course):

.. code-block:: bash

    $ pip3 install pyweathercn

