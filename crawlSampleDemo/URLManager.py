# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：    URLManager 
   Description :   URL管理器，主要包括两个变量，一个是已经爬取过的URL集合，另一个是未爬取过的URL集合。
                    采用python中的set类型进行去重，链接去重的实现方式有三种：
                        1、内存去重
                        2、关系数据库去重
                        3、缓存数据库去重（大型成熟爬虫使用的方案）
                    需要提供的接口：
                        1、判断是否有待取的URL，has_new_url()
                        2、添加新的URL到未爬取的集合中, add_new_url(url) add_new_urls(urls)
                        3、获取一个为爬取的URL，get_new_url()
                        4、获取未爬取URL集合的大小，new_url_size()
                        5、获取已爬取的URL集合大小，old_url_size()
   Author :       Administrator
   date：         2019/10/6
-------------------------------------------------

"""


class UrlManager(object):
    def __init__(self):
        self.new_urls = set()  # 未爬取集合
        self.old_urls = set()  # 已爬取集合

    def has_new_url(self):
        '''
        判断是否有未爬取的URL
        :return:
        '''
        return self.new_url_size() != 0

    def get_new_url(self):
        '''
        获取一个未爬取的URL
        :return:
        '''
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url

    def add_new_url(self, url):
        '''
        将新的URL添加到未爬取的URL集合中
        :param url:
        :return:
        '''
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)

    def add_new_urls(self, urls):
        '''
        将新的URL添加到未爬取的URL集合中
        :param urls:
        :return:
        '''
        if urls is None and len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)

    def new_url_size(self):
        return len(self.new_urls)

    def old_url_size(self):
        return len(self.old_urls)