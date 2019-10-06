# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     jsonDataTest
   Description :   将小说文档保存为json格式文件
   Author :       guodongqing
   date：          2019/10/06
-------------------------------------------------

"""

import json
from bs4 import BeautifulSoup
import requests

def jsonStorageWithHTMLParser():
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    headers = {'User-Agent': user_agent}
    r = requests.get('http://seputu.com/', headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser', from_encoding='utf-8')  # html.parser
    content = []
    for mulu in soup.find_all(class_="mulu"):
        h2 = mulu.find('h2')
        if h2 != None:
            h2_title = h2.string  # 获取标题
            list = []
            for a in mulu.find(class_='box').find_all('a'):  # 获取所有的a标签中url和章节内容
                href = a.get('href')
                box_title = a.get('title')
                list.append({'href': href, 'box_title': box_title})
            content.append({'title': h2_title, 'content': list})
    with open('小说.json', 'w') as fp:
        json.dump(content, fp=fp, indent=4, ensure_ascii=True)  # ensure_ascii=True,非ascii码会变成\uXXX

if __name__ == "__main__":
    jsonStorageWithHTMLParser()
