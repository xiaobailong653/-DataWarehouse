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
import wx.lib.agw.aui as aui

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

        self._mgr = aui.AuiManager(self)
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

    # 初始化中心窗口的部件
    def initPanes(self):
        self.leftTree = TreeCtrlHandler(self)
        self._mgr.AddPane(self.leftTree,
                          aui.AuiPaneInfo().Name("warehouse").
                          Caption("Tree Pane").Left().Layer(1).
                          Position(1).CloseButton(False).MinimizeButton(True))
        self.richtext = RichTextHandler(self)
        self._mgr.AddPane(self.richtext,
                          aui.AuiPaneInfo().Name("notebook_content").
                          CenterPane().PaneBorder(False))
        toolbar = ToolbarHandler(self)
        self._mgr.AddPane(toolbar,
                          aui.AuiPaneInfo().Name("tb2").Caption("Toolbar 2").
                          ToolbarPane().Top().Row(1))

        self._mgr.Update()

    def bindEvent(self):
        self.Bind(wx.EVT_CLOSE, self.OnClose)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUi)

    def OnClose(self, event):
        self.Destroy()

    def CreateTreeCtrl(self):
        tree = wx.TreeCtrl(self, -1, wx.Point(0, 0), wx.Size(160, 250),
                           wx.TR_DEFAULT_STYLE | wx.NO_BORDER)

        imglist = wx.ImageList(16, 16, True, 2)
        imglist.Add(wx.ArtProvider.GetBitmap(wx.ART_FOLDER, wx.ART_OTHER, wx.Size(16, 16)))
        imglist.Add(wx.ArtProvider.GetBitmap(wx.ART_NORMAL_FILE, wx.ART_OTHER, wx.Size(16, 16)))
        tree.AssignImageList(imglist)

        root = tree.AddRoot("AUI Project", 0)
        items = []

        items.append(tree.AppendItem(root, "Item 1", 0))
        items.append(tree.AppendItem(root, "Item 2", 0))
        items.append(tree.AppendItem(root, "Item 3", 0))
        items.append(tree.AppendItem(root, "Item 4", 0))
        items.append(tree.AppendItem(root, "Item 5", 0))

        for item in items:
            tree.AppendItem(item, "Subitem 1", 1)
            tree.AppendItem(item, "Subitem 2", 1)
            tree.AppendItem(item, "Subitem 3", 1)
            tree.AppendItem(item, "Subitem 4", 1)
            tree.AppendItem(item, "Subitem 5", 1)

        tree.Expand(root)

        return tree

if __name__ == '__main__':
    app = wx.App()
    frame = DataStorageFrame()
    frame.Show()
    app.MainLoop()
