#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
Created on 2014年1月21日

@author: sunlongfei
'''
import wx
import wx.lib.agw.aui as aui


class NotebookControl(aui.AuiNotebook):

    def __init__(self, parent):
        pos = (parent.GetClientSize().x, parent.GetClientSize().y)
        aui.AuiNotebook.__init__(self, parent, -1,
                                 pos=pos,
                                 agwStyle=self.getAgwStyle())
        self.SetArtProvider(aui.AuiDefaultTabArt())
        self.GetScreenPosition()
        self.Bind(wx.EVT_NOTEBOOK_PAGE_CHANGED, self.OnPageChanged)

    # 获取agw样式
    def getAgwStyle(self):
        style = aui.AUI_NB_DEFAULT_STYLE
        style |= aui.AUI_NB_TAB_EXTERNAL_MOVE
        style |= wx.NO_BORDER

        return style

    # 获取所有的孩子节点
    def getChildrenNames(self):
        children = {}
        for child in self.GetChildren():
            children[child.GetName()] = child

        return children

    def OnPageChanged(self, event):
        print 'page changed'

    def test(self):
        self.AddPage(page, caption, select, bitmap, disabled_bitmap, control)
        pass


class TestFrame(wx.Frame):

    def __init__(self):
        wx.Frame.__init__(self, None, -1, 'test')
        panel = wx.Panel(self)
        text = NotebookControl(self)


if __name__ == "__main__":
    app = wx.PySimpleApp()
    frame = TestFrame()
    frame.Show()
    app.MainLoop()
