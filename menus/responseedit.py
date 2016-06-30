#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
Created on 2014年1月10日

@author: sunlongfei
'''
################################################################
#
# 响应菜单栏中‘编辑’标签的事件
#
################################################################

import wx


class ResponseEdit():

    def __init__(self, parent):
        self.parent = parent

    # 切换编辑模式
    def OnChangeEdit(self, event):
        pass

    # 撤销
    def OnUndo(self, event):
        pass

    # 重做
    def OnRedo(self, event):
        pass

    # 剪切
    def OnCut(self, event):
        pass

    # 复制
    def OnCopy(self, event):
        pass

    # 粘贴
    def OnPaste(self, event):
        pass

    # 全选
    def OnSelect(self, event):
        pass

    # 反选
    def OnTurnSelect(self, event):
        pass

    # 删除
    def OnDelete(self, event):
        pass

    # 插入
    def OnInsert(self, event):
        pass
