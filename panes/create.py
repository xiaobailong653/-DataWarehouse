#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
Created on 2014年1月16日

@author: sunlongfei
'''
import os

import wx
import wx.grid
import wx.lib.agw.aui as aui

from panes.treectrl_cf import CFTree
from panes.treectrl_os import OSTree
from panes.notebook import NotebookControl
from panes.textctrl import TextControl
from panes.textctrl import RichTextCtrl
from panes.toolbar import ToolBar
from dmanage.config import *


def toutf8(data):
    d_list = []
    if type(data) == list:
        for l in data:
            d_list.append(l.encode('utf-8'))
    elif type(data) == unicode:
        return data.encode('utf-8')

    return d_list


class CreatePanes(aui.AuiManager):

    def __init__(self, parent):
        self.parent = parent
        aui.AuiManager.__init__(self, self.parent)
        self.left_cf_tree = None
        self.left_os_tree = None
        self.notebook = None

        self.initPane()

    def initPane(self):
        cf_path = get_section_option(self.parent.configfile,
                                     'path', 'cf_defalt_path')
        if cf_path:
            storage_name = os.path.basename(cf_path)
            self.left_cf_tree = self.addCFTree(storage_name,
                                               cf_path)

    def treePaneInfo(self, name, caption):
        return (aui.AuiPaneInfo().Name(name).
                Caption(caption).Left().Layer(1).DestroyOnClose(True).
                Position(1).CloseButton(True).MinimizeButton(True))

    def notebookPaneInfo(self, name, caption):
        return (aui.AuiPaneInfo().Name(name).
                Caption(caption).CenterPane().
                PaneBorder(False).CloseButton(True).
                MaximizeButton(True).MinimizeButton(True))

    # 绑定所有事件
    def buildEvt(self):
        self.Bind(aui.EVT_AUI_PANE_MAXIMIZE, self.OnPaneMax)
        self.Bind(aui.EVT_AUI_PERSPECTIVE_CHANGED, self.OnPaneChange)
        self.Bind(aui.EVT_AUI_PANE_RESTORE, self.OnPaneRestore)
        self.Bind(aui.EVT_AUI_PANE_DOCKED, self.OnPaneDocked)

    # 添加复合文件树控件到窗口中
    def addCFTree(self, caption, filename):
        cf_pane_info = self.treePaneInfo('TreePane', caption)
        left_cf_tree = CFTree(self.parent, filename)
        self.AddPane(left_cf_tree, cf_pane_info)
        self.GetPane('TreePane').Show().Left().Layer(0).Row(0).Position(0).DestroyOnClose(True)

        self.Update()

        return left_cf_tree

    # 添加对象存储树控件到窗口
    def addOSTree(self, caption):
        cf_pane_info = self.treePaneInfo('TreePane', caption)
        left_os_tree = OSTree(self.parent)
        self.AddPane(left_os_tree, cf_pane_info)
        self.GetPane('TreePane').Show().Left().Layer(0).Row(0).Position(0)
        self.Update()

        return left_os_tree

    # 添加Notebook控件到窗口中
    def addRighNotebook(self, caption):
        notebook_pane_info = self.notebookPaneInfo('NotebookPane', caption)
        notebook = NotebookControl(self.parent)

        self.AddPane(notebook, notebook_pane_info)

        self.GetPane('NotebookPane').Show()
        self.Update()

        return notebook

    def addRichText(self, caption):
        richtext_pane_info = self.notebookPaneInfo('richtext', caption)
        richtext = RichTextCtrl(self.parent, "richtext")
        self.AddPane(richtext, richtext_pane_info)

        self.GetPane('richtext').Show()
        self.Update()

        return richtext

    # 添加TextCtrl控件到窗口中
    def addTextCtrl(self, caption):
        text_ctrl = self.CreateTextCtrl(self.parent)
        self.AddPane(text_ctrl, aui.AuiPaneInfo().
                     Name('TextPane').Caption(caption).
                     Bottom().Layer(1).Position(1).
                     CloseButton(True).
                     MaximizeButton(True).
                     MinimizeButton(True))

        return text_ctrl

    # 添加工具栏
    def addToolBar(self, name):
        toolbar = ToolBar(self.parent)
        toolbar.initToolBar()
        self.AddPane(toolbar, aui.AuiPaneInfo().Name(name).
                     ToolbarPane().Top().Row(1).Position(1))
        self.GetPane(name).Show()
        self.Update()

        return toolbar

    # 显示指定的pane
    def show(self, panes=None):
        if panes:
            for pane in panes:
                self.GetPane(pane).Show()
        else:
            panes = self.GetAllPanes()
            for pane in panes:
                pane.Show()

        self.Update()

    # 隐藏指定的pane
    def hide(self, panes=None):
        if panes:
            for pane in panes:
                self.GetPane(pane).Hide()
        else:
            panes = self.GetAllPanes()
            for pane in panes:
                pane.Hide()

        self.Update()

    # 创建TextCtrl控件
    def CreateTextCtrl(self):

        return wx.TextCtrl(self, -1, '', wx.Point(0, 0), wx.Size(150, 90),
                           wx.NO_BORDER | wx.TE_MULTILINE)

    def closePaneItem(self):
        self.left_cf_tree.Close()
        print self.ClosePane(aui.AuiPaneInfo().Name('TreePane').Left().Layer(1).DestroyOnClose(True).
                             Position(1).CloseButton(True).MinimizeButton(True))

    def isPaneItemExist(self, name):
        panes = self.GetAllPanes()
        for pane in panes:
            if name == pane.Name():
                return True

    def OnPaneMax(self, event):
        print 'OnPaneMax'

    def OnPaneChange(self, event):
        print 'OnPaneChange'

    def OnPaneRestore(self, event):
        print 'OnPaneRestore'

    def OnPaneDocked(self, event):
        print 'OnPaneDocked'

    def OnTreeCtrlClose(self, event):
        print 'close TreeCtrl'
