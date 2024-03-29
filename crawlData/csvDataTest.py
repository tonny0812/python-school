# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：     jsonDataTest
   Description :   将小说文档保存为csv格式文件
   Author :       guodongqing
   date：          2019/10/06
-------------------------------------------------

"""


def csvWriteToFile():
    import csv
    headers = ['ID', 'UserName', 'Password', 'Age', 'Country']
    rows = [(1001, "qiye", "qiye_pass", 24, "China"),
            (1002, "Mary", "Mary_pass", 20, "USA"),
            (1003, "Jack", "Jack_pass", 20, "USA"),
            ]
    with open('test.csv', 'w') as f:
        f_csv = csv.writer(f)
        f_csv.writerow(headers)
        f_csv.writerows(rows)


def csvWriteToFile2():
    import csv
    headers = ['ID', 'UserName', 'Password', 'Age', 'Country']
    rows = [{'ID': 1001, 'UserName': "qiye", 'Password': "qiye_pass", 'Age': 24, 'Country': "China"},
            {'ID': 1002, 'UserName': "Mary", 'Password': "Mary_pass", 'Age': 20, 'Country': "USA"},
            {'ID': 1003, 'UserName': "Jack", 'Password': "Jack_pass", 'Age': 20, 'Country': "USA"},
            ]
    with open('test.csv', 'w') as f:
        f_csv = csv.DictWriter(f, headers)
        f_csv.writeheader()
        f_csv.writerows(rows)


def csvReadFromFile():
    import csv
    with open('test.csv') as f:
        f_csv = csv.reader(f)
        headers = next(f_csv)
        print(headers)
        for row in f_csv:
            print(row)


def csvReadFromFile2():
    from collections import namedtuple
    import csv
    with open('test.csv') as f:
        f_csv = csv.reader(f)
        headings = next(f_csv)
        Row = namedtuple('Row', headings)
        for r in f_csv:
            row = Row(*r)
            print(row.UserName, row.Password)
            print(row)


def csvReadFromFile3():
    import csv
    with open('test.csv') as f:
        f_csv = csv.DictReader(f)
        for row in f_csv:
            print(row.get('UserName'), row.get('Password'))


def csvStorageWithXpath():
    import requests, re, csv
    from lxml import etree

    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    headers = {'User-Agent': user_agent}
    r = requests.get('http://seputu.com/', headers=headers)
    # 使用lxml解析网页

    html = etree.HTML(r.text)
    div_mulus = html.xpath('.//*[@class="mulu"]')  # 先找到所有的div class=mulu标签
    pattern = re.compile(r'\s*\[(.*)\]\s+(.*)')
    rows = []
    for div_mulu in div_mulus:
        # 找到所有的div_h2标签
        div_h2 = div_mulu.xpath('./div[@class="mulu-title"]/center/h2/text()')
        if len(div_h2) > 0:
            h2_title = div_h2[0].encode('utf-8')
            a_s = div_mulu.xpath('./div[@class="box"]/ul/li/a')
            for a in a_s:
                # 找到href属性
                href = a.xpath('./@href')[0].encode('utf-8')
                # 找到title属性
                box_title = a.xpath('./@title')[0]

                pattern = re.compile(r'\s*\[(.*)\]\s+(.*)')
                match = pattern.search(box_title)
                if match != None:
                    date = match.group(1).encode('utf-8')
                    real_title = match.group(2).encode('utf-8')
                    # print real_title
                    content = (h2_title.decode('utf-8'), real_title.decode('utf-8'), href, date.decode('utf-8'))
                    print(content)
                    rows.append(content)
    headers = ['title', 'real_title', 'href', 'date']
    with open('小说.csv', 'w') as f:
        f_csv = csv.writer(f, )
        f_csv.writerow(headers)
        f_csv.writerows(rows)


if __name__ == "__main__":
    csvStorageWithXpath()
