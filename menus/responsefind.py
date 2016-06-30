#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
Created on 2014年1月13日

@author: sunlongfei
'''
################################################################
#
# 响应菜单栏中‘查找’标签的事件
#
################################################################

import wx


class ResponseFind():

    def __init__(self, parent):
        self.parent = parent

    # 查找
    def OnFind(self, event):
        pass

    # 查找上一个
    def OnFindLast(self, event):
        pass

    # 查找下一个
    def OnFindNext(self, event):
        pass

    # 替换
    def OnReplace(self, event):
        pass
