#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
Created on 2014年1月26日

@author: sunlongfei
'''
################################################################
#
# 响应菜单栏中‘连接’标签的事件
#
################################################################

import wx
from windows.dialog import DialogWindows
from panes.treectrl import TreeControl

from objectstorage.aliyun import Aliyun


class ResponseConnect():

    def __init__(self, parent):
        self.parent = parent

        self.dw = DialogWindows(self.parent)

    def addTreeCtrl(self, storage_name, data):
        left_tree = self.parent.panes.addOSTree(storage_name, storage_name)
        root = left_tree.addRootNode(storage_name)
        for item in data:
            left_tree.addTreeNodes(root, item['Name'])
        self.parent.panes.show([storage_name])

    def check_value(self, data):
        for key in data.keys():
            if not data[key]:
                self.dw.error_message('数据仓库', '%s不能为空' % key)
                return False
            data[key].encode('utf-8')

        return True

    def _connect_aliyun(self, data):
        if self.check_value(data):
            self.parent.aliyun = Aliyun(data['website'],
                                        data['id'],
                                        data['key'])
            buckets = self.parent.aliyun.get_all_buckets()
            self.addTreeCtrl('阿里云', buckets)

    def OnConnectAliyun(self, event):
        # 设置为对象存储
        self.parent.flag = wx.ID_NO
        dialog = ConnectDialog(self.parent, '连接阿里云存储')
        if dialog.ShowModal() == wx.ID_OK:
            data = dialog.getValue()
            data = {'website': 'oss.aliyuncs.com',
                    'id': 'HB50JO83yRE8KhLG',
                    'key': '3fAiGQ4Cu4tDeq9rCXG72P1ITcInJa'}
            self._connect_aliyun(data)
        dialog.Destroy()

    def OnConnectS3(self, event):
        pass

    def OnConnectSwift(self, event):
        pass


class NotEmptyValidator(wx.PyValidator):

    def __init__(self):
        wx.PyValidator.__init__(self)

#     def Clone(self):
#         return NotEmptyValidator()

    def Validate(self, win):
        textCtrl = self.GetWindow()
        text = textCtrl.GetValue()
        if len(text) == 0:
            wx.MessageBox('This field must contain some text!', 'Error')
            textCtrl.SetBackgroundColour('pink')
            textCtrl.SetFocus()
            textCtrl.Refresh()
            return False
        else:
            textCtrl.SetBackgroundColour(wx.SystemSettings_GetColour(wx.SYS_COLOUR_WINDOW))
            textCtrl.Refresh()
            return True


class ConnectDialog(wx.Dialog):

    def __init__(self, parent, title):
        wx.Dialog.__init__(self, parent, -1, title, size=(600, 300))
        self.st_size = (100, 30)
        self.st_style = wx.TE_RIGHT
        self.tc_size = (250, 30)
        self.tc_style = wx.TE_LEFT
        self.initStaticText()
        self.initTextCtrl()
        self.initButton()
        self.setSizer()

    def initStaticText(self):
        self.st_website = wx.StaticText(self, -1, 'website:', size=self.st_size, style=self.st_style)
        self.st_ID = wx.StaticText(self, -1, 'ID:', size=self.st_size, style=self.st_style)
        self.st_key = wx.StaticText(self, -1, 'KEY:', size=self.st_size, style=self.st_style)

    def initTextCtrl(self):
        self.tc_website = wx.TextCtrl(self, size=self.tc_size, style=self.tc_style,
                                      validator=NotEmptyValidator())
        self.tc_ID = wx.TextCtrl(self, size=self.tc_size, style=self.tc_style,
                                 validator=NotEmptyValidator())
        self.tc_key = wx.TextCtrl(self, size=self.tc_size, style=self.tc_style,
                                  validator=NotEmptyValidator())

    def initButton(self):
        self.okay = wx.Button(self, wx.ID_OK, "连接")
        self.okay.SetDefault()
        self.cancel = wx.Button(self, wx.ID_CANCEL, '取消')

    def setSizer(self):
        sizer = wx.BoxSizer(wx.VERTICAL)
        fgs = wx.FlexGridSizer(3, 2, 5, 5)
        fgs.Add(self.st_website, 0, wx.ALIGN_RIGHT)
        fgs.Add(self.tc_website, 0, wx.EXPAND)
        fgs.Add(self.st_ID, 0, wx.ALIGN_RIGHT)
        fgs.Add(self.tc_ID, 0, wx.EXPAND)
        fgs.Add(self.st_key, 0, wx.ALIGN_RIGHT)
        fgs.Add(self.tc_key, 0, wx.EXPAND)
        fgs.AddGrowableCol(1)
        sizer.Add(fgs, 0, wx.EXPAND | wx.ALL, 5)
        btns = wx.StdDialogButtonSizer()
        btns.AddButton(self.okay)
        btns.AddButton(self.cancel)
        btns.Realize()
        sizer.Add(btns, 0, wx.EXPAND | wx.ALL, 5)
        self.SetSizer(sizer)
        sizer.Fit(self)

    def getValue(self):
        data = {}
        data['website'] = self.tc_website.GetValue()
        data['id'] = self.tc_ID.GetValue()
        data['key'] = self.tc_key.GetValue()

        return data

if __name__ == '__main__':
    app = wx.PySimpleApp()
    dialog = ConnectDialog(None, 'sfsf')
    dialog.ShowModal()
    dialog.Destroy()
    app.MainLoop()
