#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
Created on 2014年1月21日

@author: sunlongfei
'''
import wx
from PIL import Image as images
import wx.lib.agw.aui as aui
import wx.richtext as richtext


class TextControl(wx.TextCtrl):

    def __init__(self, parent, name):
        style = wx.TE_MULTILINE | wx.TE_RICH2 | wx.TE_RICH
        wx.TextCtrl.__init__(self, parent, -1, style=style, name=name)

    def getCurrentFont(self):
        attr = wx.TextAttr()
        # attr.SetFlags(wx.TEXT_ATTR_FONT)
        if self.GetStyle(self.GetInsertionPoint(), attr):
            return attr.GetFont()
        else:
            return None

    def isSelectionBold(self):
        font = self.getCurrentFont()
        if font != None:
            if font.GetWeight() == wx.BOLD:
                return True

        return False

    def isSelectionItalic(self):
        font = self.getCurrentFont()
        if font != None:
            if font.GetStyle == wx.ITALIC:
                return True

        return False

    def test(self):
        f = self.GetFont()

        print f.GetWeightString()


class RichTextCtrl(richtext.RichTextCtrl):

    def __init__(self, parent, name):
        style = wx.TE_MULTILINE | wx.NO_BORDER
        richtext.RichTextCtrl.__init__(self, parent, -1, style=style, name=name)


class AuiNotePage(aui.AuiNotebookPage):

    def __init__(self, parent, name):
        pass


class TestFrame(wx.Frame):

    def __init__(self):
        wx.Frame.__init__(self, None, -1, 'test', size=(700, 500), style=wx.DEFAULT_FRAME_STYLE)
        text = TextControl(self, 'test')

        text.test()


if __name__ == "__main__":
    app = wx.PySimpleApp()
    frame = TestFrame()
    frame.Show()
    app.MainLoop()
