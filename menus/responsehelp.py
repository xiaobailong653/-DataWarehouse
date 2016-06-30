#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
Created on 2014年1月13日

@author: sunlongfei
'''
################################################################
#
# 响应菜单栏中‘帮助’标签的事件
#
################################################################

import wx


class ResponseHelp():

    def __init__(self, parent):
        self.parent = parent

    # 使用说明
    def OnHelpContents(self, event):
        pass

    # 更新
    def OnUpdate(self, event):
        pass

    # 技术支持
    def OnSupport(self, event):
        pass

    # 常见的问题
    def OnQuestion(self, event):
        pass

    # 联系我们
    def OnkContact(self, event):
        pass

    # 注册
    def OnRegister(self, event):
        pass

    # 关于
    def OnAbout(self, event):
        pass
