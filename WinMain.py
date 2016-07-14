# -*- coding: utf8 -*-
#################################################
# Create By : sunlf
#
# Create On : 2016-06-29
#
# Comment : DataWarehouse
#################################################


import os

import wx
import wx.aui
import wx.lib.agw.aui as aui

from menus.create import CreateMenu
from toolbar.create import CreateToolBar
from panes.create import CreatePanes
from windows.dialog import DialogWindows
from dmanage.config import *
from panes.textctrl import RichTextCtrl

from menus.menuBar import MenuBarHandler
from pane import TreeCtrlHandler
from pane import RichTextHandler
from pane import ToolbarHandler


class DataStorageFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1,
                          u'数据仓库',
                          size=(1024, 600),
                          pos=(50, 0))

        self._aui = wx.aui.AuiManager(self)
        # self.dlg = DialogWindows(self)

        # 设置默认为数据仓库
        # self.flag = wx.ID_OK

        # 设置配置文件路径
        # self.configfile = './dmanage/config.txt'

        self.initFrame()
        # self.initConfig()

    # 初始化窗口
    def initFrame(self):
        # 设置窗口最小值
        self.SetMinSize(wx.Size(400, 300))
        # 初始化各个部件
        
        self.initStatusBar()
        self.initPanes()
        self.initMenuBar()

    # 初始化标题栏
    def initMenuBar(self):
        menubar = MenuBarHandler(self)
        self.SetMenuBar(menubar)

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
        self.leftTree = TreeCtrlHandler(self)
        self._aui.AddPane(self.leftTree,
                          wx.aui.AuiPaneInfo().Left().
                          MaximizeButton().CloseButton(False))
        self.richtext = RichTextHandler(self)
        self._aui.AddPane(self.richtext, wx.aui.AuiPaneInfo().Center())
        self.toolbar = ToolbarHandler(self)
        self._aui.AddPane(self.toolbar, wx.aui.AuiPaneInfo().Name("toolbar").ToolbarPane().Top())

        self._aui.Update()

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
