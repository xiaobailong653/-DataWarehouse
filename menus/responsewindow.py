#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
Created on 2014年1月13日

@author: sunlongfei
'''
################################################################
#
# 响应菜单栏中‘窗口’标签的事件
#
################################################################

import wx


class ResponseWindow():

    def __init__(self, parent):
        self.parent = parent

    # 打开窗口
    def OnOpenWindow(self, event):
        pass

    # 关闭当前窗口
    def OnCloseWindow(self, event):
        pass

    # 关闭所有打开的窗口
    def OnCloseAllWindows(self, event):
        pass

    # 层叠排列窗口
    def OnStackWindows(self, event):
        pass

    # 水平排列窗口
    def OnHorizontalWindows(self, event):
        pass

    # 垂直排列窗口
    def OnVerticalWindows(self, event):
        pass

    # 排列图标
    def OnArrangeIcon(self, event):
        pass

    # 切换窗口
    def OnChangeWindow(self, event):
        pass
