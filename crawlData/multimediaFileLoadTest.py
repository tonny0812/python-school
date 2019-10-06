# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：    multimediaFileLoadTest 
   Description :   多媒体文件
   Author :       Administrator
   date：         2019/10/6
-------------------------------------------------

"""


# python2
def downloadImg():
    import urllib
    from lxml import etree
    import requests
    def Schedule(blocknum, blocksize, totalsize):
        '''''
        blocknum:已经下载的数据块
        blocksize:数据块的大小
        totalsize:远程文件的大小
        '''
        per = 100.0 * blocknum * blocksize / totalsize
        if per > 100:
            per = 100
        print('当前下载进度：%d' % per)

    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    headers = {'User-Agent': user_agent}
    r = requests.get('http://www.ivsky.com/tupian/ziranfengguang/', headers=headers)
    # 使用lxml解析网页
    html = etree.HTML(r.text)
    img_urls = html.xpath('.//img/@src')  # 先找到所有的img
    i = 0
    for img_url in img_urls:
        img_url = 'https:' + img_url
        urllib.urlretrieve(img_url, 'images/img_' + str(i) + '.jpg', Schedule)
        i += 1


# python3
def downloadImg2():
    import urllib.request
    import sys, os
    from lxml import etree
    def callbackfunc(blocknum, blocksize, totalsize):
        '''回调函数
        @blocknum: 已经下载的数据块
        @blocksize: 数据块的大小
        @totalsize: 远程文件的大小
        '''
        percent = 100.0 * blocknum * blocksize / totalsize
        if percent > 100:
            percent = 100
        downsize = blocknum * blocksize
        if downsize >= totalsize:
            downsize = totalsize
        s = "%.2f%%" % (percent) + "====>" + "%.2f" % (downsize / 1024 / 1024) + "M/" + "%.2f" % (
                totalsize / 1024 / 1024) + "M \r"
        sys.stdout.write(s)
        sys.stdout.flush()
        if percent == 100:
            print('')
            input("下载完成（按任意键继续...）")

    def downimg(url):
        input("下载：%s（按任意键继续...）" % img_url)
        filename = 'images/' + os.path.basename(url)
        urllib.request.urlretrieve(url, filename, callbackfunc)

    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    headers = {'User-Agent': user_agent}
    req = urllib.request.Request(url='http://www.ivsky.com/tupian/ziranfengguang/index_2.html', data={}, headers=headers)
    response = urllib.request.urlopen(req)
    # 使用lxml解析网页
    html = etree.HTML(response.read())
    img_urls = html.xpath('.//img/@src')  # 先找到所有的img
    for img_url in img_urls:
        img_url = 'https:' + img_url
        downimg(img_url)

if __name__ == "__main__":
    downloadImg2()
