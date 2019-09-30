# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     coroutineTest
   Description :   协程，微线程，使用第三方库：gevent
   Author :       guodongqing
   date：          2019/9/30
-------------------------------------------------

"""
from gevent import monkey
monkey.patch_all()

import gevent as gevent


def run_task(url):
    from urllib import request
    print(u"访问-->>%s" % url)
    try:
        response = request.urlopen(url)
        data = response.read()
        print(u"从(%s) ---->>>接收数据大小：%d 字节..." % (url, len(data)))
    except Exception as e:
        print(e)


if __name__ == "__main__":
    urls = ['https://www.github.com', 'https://www.python.org', 'https://www.baidu.com', 'http://www.cnblogs.com']
    greenlets = [gevent.spawn(run_task, url) for url in urls]
    gevent.joinall(greenlets)
