# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     IOTest
   Description :
   Author :       guodongqing
   date：          2019/9/30
-------------------------------------------------
"""

with open(file=r"test.txt", mode="w", encoding="UTF-8") as fileWrapper:
    fileWrapper.write("测试")

with open(file=r"test.txt", mode="r", encoding="UTF-8") as fileReader:
    for line in fileReader.readlines():
        print(line.strip())
