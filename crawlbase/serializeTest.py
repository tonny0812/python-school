# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     serializeTest
   Description :
   Author :       guodongqing
   date：          2019/9/30
-------------------------------------------------
"""

try:
    import cPickle as pickle
except ImportError:
    import pickle

d = dict(url = "index.hmtl", title = "首页", content = "首页内容")
pickle.dumps(d)

with open(file=r"dump.txt", mode="wb") as flieWriter:
    pickle.dump(d, flieWriter)

with open(file=r"dump.txt", mode="rb") as fileReader:
    d = pickle.load(fileReader)
    print(d)