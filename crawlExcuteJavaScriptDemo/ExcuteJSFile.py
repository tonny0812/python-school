# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     ExcuteJSFile
   Description :   python中执行js代码
   Author :       guodongqing
   date：          2019/10/10
-------------------------------------------------
"""

import execjs
import js2py


def getJSFileContent(filePath):
    with open(filePath) as f:
        jsdata = f.read()
        # print(jsdata)
    return jsdata


def excuteJSFileFunction1(filePath, fun, *args):
    jsdata = getJSFileContent(filePath)
    ctx = execjs.compile(jsdata)
    return ctx.call(fun, *args)


def excuteJSFileFunction2(filePath, *args):
    jsdata = getJSFileContent(filePath)
    context = js2py.EvalJs()
    context.execute(jsdata)
    return context.sum(*args)


if __name__ == "__main__":
    result = excuteJSFileFunction1('js/fuck-byted-acrawler.js', 'generateSignature', '12345')
    print(result)
    result = excuteJSFileFunction1('js/test.js', 'sum', 12, 3)
    print(result)
    result = excuteJSFileFunction2('js/test.js', '1', '12345', '00000')
    print(result)
