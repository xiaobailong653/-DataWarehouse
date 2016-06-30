#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
Created on 2014年1月14日

@author: sunlongfei
'''


def display_list(message):
    ll = []
    for i in range(0, len(message)-1):
        ll.append(message[i])
        if ll % 5 == 0:
            print ll
            ll = []
    print ll


def wx_help(message):
    print help(message)


def wx_dir(message):
    ll = dir(message)
    for i in range(0, len(ll)):
        print ll[i:i+5]
        i += 5
