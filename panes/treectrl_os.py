#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
Created on 2014年1月26日

@author: sunlongfei
'''
import wx

from dmanage.textdata import TextData
from panes.textctrl import TextControl

data_tree = ''


class OSTree(wx.TreeCtrl):

    def __init__(self, parent):
        self.parent = parent
        wx.TreeCtrl.__init__(self, parent, -1, wx.Point(0, 0), (200, 250),
                             wx.TR_DEFAULT_STYLE | wx.NO_BORDER | wx.TR_HIDE_ROOT)
        self.iconsInit()
        self.buildEvt()

    def iconsInit(self):
        icons = wx.ImageList(16, 16)
        self.fldridx = icons.Add(wx.ArtProvider.GetBitmap(wx.ART_FOLDER, wx.ART_OTHER, (16, 16)))
        self.fldropenidx = icons.Add(wx.ArtProvider.GetBitmap(wx.ART_NORMAL_FILE, wx.ART_OTHER, (16, 16)))
        self.fileidx = icons.Add(wx.ArtProvider.GetBitmap(wx.ART_NORMAL_FILE, wx.ART_OTHER, (16, 16)))
        self.AssignImageList(icons)

    def buildEvt(self):
        self.Bind(wx.EVT_TREE_ITEM_RIGHT_CLICK, self.OnRightClick)
        self.Bind(wx.EVT_TREE_ITEM_ACTIVATED, self.OnActivated)

    def addRootNode(self, name):
        root = self.AddRoot(name)
        self.SetItemImage(root, self.fldridx, wx.TreeItemIcon_Normal)  # 设置根图像
        self.SetItemImage(root, self.fldropenidx, wx.TreeItemIcon_Expanded)

        return root

    def addTreeNodes(self, parentItem, items):
        if type(items) == list:
            for item in items:
                if type(item) == list:
                    newItem = self.AppendItem(parentItem, item[0])
                    self.SetItemImage(newItem, self.fldridx, wx.TreeItemIcon_Normal)
                    self.SetItemImage(newItem, self.fldropenidx, wx.TreeItemIcon_Expanded)
                    self.AddTreeNodes(newItem, item[1])
                else:
                    newItem = self.AppendItem(parentItem, item)
                    self.SetItemImage(newItem, self.fileidx, wx.TreeItemIcon_Normal)
        else:
            newItem = self.AppendItem(parentItem, items)
            self.SetItemImage(newItem, self.fileidx, wx.TreeItemIcon_Normal)

        # self.Expand(parentItem)

    def menuOSData(self):
        return (('&上传文件', '在当前节点下增加子节点', self.OnUpload),
                ('&下载文件', '在当前节点下增加子节点', self.OnDownload),
                ('', '', ''),
                ('&剪切', '剪切当前节点', self.OnCutFile),
                ('&复制', '复制当前节点', self.OnCopyFile),
                ('&粘贴', '粘贴节点成为当前节点的子节点', self.OnPasteFile),
                ('', '', ''),
                ('&删除', '删除当前节点', self.OnDelFile),
                ('', '', ''),)

    def createMenu(self, menuData):
        menu = wx.Menu()
        for eachItem in menuData:
            if eachItem[0]:
                item = menu.Append(-1, eachItem[0], eachItem[1])
                self.parent.Bind(wx.EVT_MENU, eachItem[2], item)
            else:
                menu.AppendSeparator()

        return menu

    def getItemText(self, item):
        if item:
            return self.GetItemText(item)
        else:
            return ''

    def OnRightClick(self, event):
        self.SelectItem(event.GetItem())  # 设置选中的Item
        menuData = self.menuOSData()
        self.menu = self.createMenu(menuData)
        self.PopupMenu(self.menu)
        event.Skip()

    def OnActivated(self, event):
        item = self.getItemText(event.GetItem())
        if self.parent.flag == wx.ID_OK:
            self._composite_file(item)
        else:
            self._object_storage(item)
        event.Skip()

    def OnUpload(self, event):
        print 'OnActivated'

    def OnDownload(self, event):
        print 'OnActivated'

    def OnCutFile(self, event):
        print 'OnActivated'

    def OnCopyFile(self, event):
        print 'OnActivated'

    def OnPasteFile(self, event):
        print 'OnActivated'

    def OnDelFile(self, event):
        print 'OnActivated'
