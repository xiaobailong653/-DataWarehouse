#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
Created on 2014年1月13日

@author: sunlongfei
'''
################################################################
#
# 响应菜单栏中‘段落’标签的事件
#
################################################################

import wx


class ResponseParagraph():

    def __init__(self, parent):
        self.parent = parent

    # 左对齐
    def OnLeftAlign(self, event):
        pass

    # 右对齐
    def OnRightAlign(self, event):
        pass

    # 居中
    def OnMiddle(self, event):
        pass

    # 两端对齐
    def OnTwoEndsAlign(self, event):
        pass

    # 增加缩进
    def OnAddIndentation(self, event):
        pass

    # 减少缩进
    def OnReduceIndentation(self, event):
        pass

    # 自定义缩进
    def OnCustomIndentation(self, event):
        pass

    # 1倍行距
    def OnOneLineSpace(self, event):
        pass

    # 1.5倍行距
    def OnOneHalfLineSpace(self, event):
        pass

    # 两倍行距
    def OnTwoLineSpace(self, event):
        pass

    # 段落间距
    def OnParagraphSpace(self, event):
        pass
