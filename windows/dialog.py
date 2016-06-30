#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
Created on 2014年1月21日

@author: sunlongfei
'''
import wx


class DialogWindows():

    def __init__(self, parent):
        self.parent = parent
        self.style = wx.YES_NO
        self.info_style = self.style | wx.ICON_INFORMATION
        self.question_style = self.style | wx.ICON_QUESTION
        self.waring_style = self.style | wx.ICON_EXCLAMATION
        self.error_style = self.style | wx.ICON_ERROR

    def info_message(self, title, content):
        dialog = wx.MessageDialog(self.parent, content, title, self.info_style)
        result = dialog.ShowModal()
        dialog.Destroy()

        return result

    def question_message(self, title, content, style=0):
        dialog = wx.MessageDialog(self.parent, content, title, self.question_style | style)
        result = dialog.ShowModal()
        dialog.Destroy()

        return result

    def waring_message(self, title, content):
        dialog = wx.MessageDialog(self.parent, content, title, self.waring_style)
        result = dialog.ShowModal()
        dialog.Destroy()

        return result

    def error_message(self, title, content):
        dialog = wx.MessageDialog(self.parent, content, title, self.error_style)
        result = dialog.ShowModal()
        dialog.Destroy()

        return result

if __name__ == "__main__":
    app = wx.PySimpleApp()
    dlg = DialogWindows(None)
    print dlg.question_message('dialog', 'hello world')
    app.MainLoop()
