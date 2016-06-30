#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
Created on 2014年1月13日

@author: sunlongfei
'''
################################################################
#
# 响应菜单栏中‘格式’标签的事件
#
################################################################

import wx


class ResponseFormat():

    def __init__(self, parent):
        self.parent = parent

    def getCurrentPage(self):
        notebook = self.parent.getNotebookHandle()
        page_idx = notebook.GetSelection()
        if page_idx != -1:
            page = notebook.GetPage(page_idx)
            return page
        return ''

    # 字体
    def OnFont(self, event):
        page = self.getCurrentPage()
        if page:
            start, end = page.GetSelection()
            fontData = wx.FontData()
            fontData.EnableEffects(False)
            attr = wx.TextAttr()
            attr.SetFlags(wx.TEXT_ATTR_FONT)
            if page.GetStyle(page.GetInsertionPoint(), attr):
                fontData.SetInitialFont(attr.GetFont())

            dlg = wx.FontDialog(self.parent, fontData)
            if dlg.ShowModal() == wx.ID_OK:
                fontData = dlg.GetFontData()
                font = fontData.GetChosenFont()
                if font:
                    attr.SetFlags(wx.TEXT_ATTR_FONT)
                    attr.SetFont(font)
                    page.SetStyle(start, end, attr)
            dlg.Destroy()

    # 设置字体加粗
    def OnFontBold(self, event):
        pass

    # 斜体
    def OnFontItalic(self, event):
        pass

    # 下划线
    def OnFontUnderline(self, event):
        pass

    # 删除线
    def OnFontDeleteline(self, event):
        pass

    # 设置字体颜色
    def OnFontColour(self, event):
        page = self.getCurrentPage()
        if page:
            colourData = wx.ColourData()
            attr = wx.TextAttr()
            attr.SetFlags(wx.TEXT_ATTR_TEXT_COLOUR)
            if page.GetStyle(page.GetInsertionPoint(), attr):
                colourData.SetColour(attr.GetTextColour())

            dlg = wx.ColourDialog(self.parent, colourData)
            if dlg.ShowModal() == wx.ID_OK:
                colourData = dlg.GetColourData()
                colour = colourData.GetColour()
                if colour:
                    print colour
                    start, end = page.GetSelection()
                    attr.SetFlags(wx.TEXT_ATTR_TEXT_COLOUR)
                    attr.SetTextColour(colour)
                    page.SetStyle(start, end, attr)
            dlg.Destroy()

    # 背景颜色
    def OnBackgroudColour(self, event):
        page = self.getCurrentPage()
        if page:
            colourData = wx.ColourData()
            colour = page.GetBackgroundColour()
            colourData.SetColour(colour)

            dlg = wx.ColourDialog(self.parent, colourData)
            if dlg.ShowModal() == wx.ID_OK:
                colourData = dlg.GetColourData()
                colour = colourData.GetColour()
                if colour:
                    page.SetBackgroundColour(colour)
            dlg.Destroy()

    # 高亮
    def OnHighLight(self, event):
        pass

    # 编辑超级链接
    def OnEditHyperlink(self, event):
        pass

    # 取消超级链接
    def OnDeleteHyperlink(self, event):
        pass
