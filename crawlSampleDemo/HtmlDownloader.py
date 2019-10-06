# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：    HtmlDownloader 
   Description :   HTML下载器，需要考虑页面编码，实现一个接口downlaod(url)
   Author :       Administrator
   date：         2019/10/6
-------------------------------------------------

"""
import urllib.request


class HtmlDownloader(object):

    def download(self, url, data=None):
        if url is None:
            return None
        user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        headers = {'User-Agent': user_agent}
        req = urllib.request.Request(url=url, data=data, headers=headers)
        res = urllib.request.urlopen(req)
        if res.getcode() == 200:
            return res.read()
        return None
