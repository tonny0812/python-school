# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     mega
   Description :
                    https://github.com/richardARPANET/mega.py
   Author :       guodongqing
   date：          2019/10/28
-------------------------------------------------
"""
from megaapi.mega.mega import Mega


def test():
    """
    Enter your account details to begin
    comment/uncomment lines to test various parts of the API
    see readme.md for more information
    """

    # user details
    email = 'guodq***@163.com'
    password = '****'

    mega = Mega()
    # mega = Mega({'verbose': True})  # verbose option for print output

    # login
    m = mega.login(email, password)

    # get user details
    details = m.get_user()
    print(details)

if __name__ == '__main__':
    test()
