#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
Created on 2014年2月14日

@author: sunlongfei
'''
################################################################
#
# 响应菜单栏中‘工具’标签的事件
#
################################################################

import wx
import json
import codecs


class ResponseTools():

    def __init__(self, parent):
        self.parent = parent
        self.indent = 2

    def OnDisplayJson(self, event):
        jsonFrame = JsonFrame(self.parent, self.indent)
        jsonFrame.Show()

    def OnDisplaySetting(self, event):
        dissetting = wx.Dialog(self.parent, -1, '数据仓库-Json格式化显示设置',
                               size=(400, 300), pos=(250, 50))
        wx.Button(dissetting, wx.ID_OK, '确定', pos=(50, 150))
        wx.Button(dissetting, wx.ID_CANCEL, '取消', pos=(250, 150))
        indentList = ["0", "1", "2", "3", "4", "5", ]
        wx.StaticText(dissetting, -1, "缩进空格数：", (20, 20))
        choice = wx.Choice(dissetting, -1, (100, 18), choices=indentList)
        choice.SetSelection(self.indent)
        if wx.ID_OK == dissetting.ShowModal():
            self.indent = choice.GetSelection()


class JsonFrame(wx.Frame):

    def __init__(self, parent, indent):
        wx.Frame.__init__(self, parent, -1, '数据仓库-Json格式化显示', size=(800, 600), pos=(250, 50))
        self.panel = wx.Panel(self, -1)
        self.indent = indent
        self.basicText = wx.TextCtrl(self.panel, -1, '')
        self.basicText.SetInsertionPoint(0)
        self.ok_button = wx.Button(self.panel, -1, '确定')
        self.clear_button = wx.Button(self.panel, -1, '清除')
        self.Bind(wx.EVT_BUTTON, self.OnOk, self.ok_button)
        self.Bind(wx.EVT_BUTTON, self.OnClear, self.clear_button)
        self.ok_button.SetDefault()
        self.multiText = wx.TextCtrl(self.panel, -1, '',
                                     size=(780, 528), style=wx.TE_MULTILINE, pos=(10, 35))

        self.multiText.SetInsertionPoint(0)
        self.addSizer()

    def addSizer(self):
        sizer = wx.GridBagSizer(hgap=3, vgap=2)
        sizer.Add(self.basicText, pos=(0, 0), span=(1, 1), flag=wx.EXPAND)
        sizer.Add(self.ok_button, pos=(0, 1), flag=wx.FIXED_MINSIZE)
        sizer.Add(self.clear_button, pos=(0, 2), flag=wx.FIXED_MINSIZE)
        sizer.Add(self.multiText, pos=(1, 0), span=(1, 3), flag=wx.EXPAND)
        sizer.AddGrowableCol(3)
        sizer.AddGrowableRow(3)
        self.panel.SetSizer(sizer)

    def OnOk(self, event):
        value = self.basicText.GetValue()
        try:
            content = json.loads(value)
            data = json.dumps(content, indent=self.indent,
                              ensure_ascii=False)  # 显示汉字设置
            self.multiText.SetValue(data)
        except ValueError:  # 如果不是Json格式的数据，就原始返回
            self.multiText.SetValue(value)

    def OnClear(self, event):
        self.basicText.SetValue('')
        self.multiText.SetValue('')


class JsonSetFrame(wx.Dialog):

    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, -1, '数据仓库-Json格式化显示设置',
                           size=(400, 300), pos=(250, 50))
        panel = wx.Panel(self, -1)
        self.btOK = wx.Button(panel, -1, '确定', pos=(50, 150))
        self.Bind(wx.EVT_BUTTON, self.OnClickOK, self.btOK)
        self.btCancel = wx.Button(panel, -1, '取消', pos=(250, 150))
        self.Bind(wx.EVT_BUTTON, self.OnClickCancel, self.btCancel)
        sizer = wx.GridBagSizer(hgap=5, vgap=5)
        indentList = ["0", "1", "2", "3", "4", "5", ]
        self.indent = 0
        wx.StaticText(panel, -1, "缩进空格数：", (20, 20))
        self.choice = wx.Choice(panel, -1, (100, 18), choices=indentList)
        self.choice.SetSelection(0)

    def getIndent(self):
        return self.indent

    def OnClickOK(self, event):
        self.indent = self.choice.GetSelection()
        self.Close()

    def OnClickCancel(self, event):
        self.Close()

if __name__ == "__main__":
    app = wx.PySimpleApp()
    frame = JsonFrame(None, 2)
    frame.Show()
    app.MainLoop()
