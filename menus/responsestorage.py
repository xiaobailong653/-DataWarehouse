#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
Created on 2014年1月10日

@author: sunlongfei
'''
################################################################
#
# 响应菜单栏中‘仓库’标签的事件
#
################################################################

import wx


class ResponseStorage():

    def __init__(self, parent):
        self.parent = parent

    # 插入子节点
    def OnAddChildNode(self, event):
        cf_tree = self.parent.getCFTreeHandle()
        cf_tree.OnAddChildNode(event)

    # 向前插入节点
    def OnAddBefNode(self, event):
        cf_tree = self.parent.getCFTreeHandle()
        cf_tree.OnAddBefNode(event)

    # 向后插入节点
    def OnAddAftNode(self, event):
        cf_tree = self.parent.getCFTreeHandle()
        cf_tree.OnAddAftNode(event)

    # 剪切节点
    def OnCut(self, event):
        cf_tree = self.parent.getCFTreeHandle()
        cf_tree.OnCut(event)

    # 复制节点
    def OnCopy(self, event):
        cf_tree = self.parent.getCFTreeHandle()
        cf_tree.OnCopy(event)

    # 粘贴节点
    def OnPaste(self, event):
        cf_tree = self.parent.getCFTreeHandle()
        cf_tree.OnPaste(event)

    # 删除节点
    def OnDelNode(self, event):
        cf_tree = self.parent.getCFTreeHandle()
        cf_tree.OnDelNode(event)

    # 节点上移
    def OnMoveUp(self, event):
        cf_tree = self.parent.getCFTreeHandle()
        cf_tree.OnMoveUp(event)

    # 节点下移
    def OnMoveDown(self, event):
        cf_tree = self.parent.getCFTreeHandle()
        cf_tree.OnMoveDown(event)

    # 节点左移
    def OnMoveLeft(self, event):
        cf_tree = self.parent.getCFTreeHandle()
        cf_tree.OnMoveLeft(event)

    # 节点右移
    def OnMoveRight(self, event):
        cf_tree = self.parent.getCFTreeHandle()
        cf_tree.OnMoveRight(event)
