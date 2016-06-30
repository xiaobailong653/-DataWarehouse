#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
Created on 2014年1月10日

@author: sunlongfei
'''
import os

import wx
import wx.lib.agw.aui as aui

from menus.create import CreateMenu
from toolbar.create import CreateToolBar
from panes.create import CreatePanes
from windows.dialog import DialogWindows
from dmanage.config import *
from panes.textctrl import RichTextCtrl


class DataStorageFrame(wx.Frame):

    def __init__(self):
        wx.Frame.__init__(self, None, -1,
                          '数据仓库',
                          size=(1024, 600),
                          pos=(50, 0))

        self.dlg = DialogWindows(self)

        # 设置默认为数据仓库
        self.flag = wx.ID_OK

        # 设置配置文件路径
        self.configfile = './dmanage/config.txt'

        self.initFrame()
        self.initConfig()

    # 初始化窗口
    def initFrame(self):
        # 设置窗口最小值
        self.SetMinSize(wx.Size(400, 300))
        # 初始化各个部件
        self.initMenuBar()
        self.initStatusBar()
        self.initPanes()
        self.initObjectStorage()

    # 初始化标题栏
    def initMenuBar(self):
        self.menu = CreateMenu(self)

    # 初始化状态栏
    def initStatusBar(self):
        self.statusbar = self.CreateStatusBar()
        self.statusbar.SetFieldsCount(3)
        self.statusbar.SetStatusWidths([-2, -2, -1])

    # 初始化工具栏
    def initToolBar(self):
        pass
        # self.toolbar = CreateToolBar(self)

    # 初始化中心窗口的部件
    def initPanes(self):
        self.panes = CreatePanes(self)
        #self.notebook = self.panes.addRighNotebook('notebook')
        self.richtext = self.panes.addRichText('richtext')
        self.tb1 = self.panes.addToolBar('tb1')
        self.cf_tree = None
        self.os_tree = None

    def initObjectStorage(self):
        self.aliyun = None
        self.s3 = None
        self.swift = None

    def configData(self):
        return {'path': {
            'cf_defalt_path': '',
            'cf_defalt': ''},
            'displayjson': {
            'colour': '',
            'indent': ''}
        }

    def initConfig(self):
        if not os.path.exists(self.configfile):
            create_configfile(self.configfile, self.configData())

    def bindEvent(self):
        self.Bind(wx.EVT_CLOSE, self.OnClose)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUi)

    def getPaneHandle(self):
        return self.panes

    def getCFTreeHandle(self):
        return self.panes.left_cf_tree

    def getOSTreeHandle(self):
        return self.panes.left_os_tree

    def getNotebookHandle(self):
        return self.notebook

    def getToolbarHandle(self):
        return self.tb1

    def OnClose(self, event):
        content = '以下数据仓库已经做修改， 是否保存修改到数据仓库？'
        result = self.dlg.question_message('数据仓库', content, wx.CANCEL)
        if result == wx.ID_NO:
            self.Destroy()
        elif result == wx.ID_YES:
            print '保存数据'
            self.Destroy()

    def OnUpdateUi(self, event):
        print 'Update ui'


if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = DataStorageFrame()
    frame.Show()
    app.MainLoop()
