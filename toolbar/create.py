#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
Created on 2014年1月16日

@author: sunlongfei
'''
import wx
from PIL import Image as images


class CreateToolBar():

    def __init__(self, parent):
        self.parent = parent
        self.aui_manager = parent.aui_manager
        self.createToolBar()

    # 工具栏的数据
    def toolData(self):
        return ((-1, images._rt_open.getBitmap(), '打开', self.OnOpenFile),
                ('', '', '', ''),
                (-1, images._rt_save.getBitmap(), '保存', self.OnSave),
                (-1, images._rt_smiley.getBitmap(), '保存全部', self.OnSaveAll),
                ('', '', '', ''),
                (wx.ID_CUT, images._rt_cut.getBitmap(), '剪切', self.OnCut),
                (wx.ID_COPY, images._rt_copy.getBitmap(), '复制', self.OnCopy),
                (wx.ID_PASTE, images._rt_paste.getBitmap(), '粘贴', self.OnPaste),
                ('', '', '', ''),
                (wx.ID_UNDO, images._rt_undo.getBitmap(), '撤销', self.OnUndo),
                (wx.ID_REDO, images._rt_redo.getBitmap(), '重做', self.OnRedo),
                ('', '', '', ''),
                (-1, images._rt_bold.getBitmap(), '加粗', self.OnBold),
                (-1, images._rt_italic.getBitmap(), '斜体', self.OnItalic),
                (-1, images._rt_underline.getBitmap(), '下划线', self.OnUnderline),
                ('', '', '', ''),
                (-1, images._rt_alignleft.getBitmap(), '左对齐', self.OnAlignLeft),
                (-1, images._rt_centre.getBitmap(), '居中', self.OnALignCentre),
                (-1, images._rt_alignright.getBitmap(), '右对齐', self.OnAlignRight),
                ('', '', '', ''),
                (-1, images._rt_font.getBitmap(), '字体', self.OnFont),
                (-1, images._rt_colour.getBitmap(), '颜色', self.OnColour),
                ('', '', '', ''),
                )

    # 创建工具栏
    def createToolBar(self):
        toolbar = self.parent.CreateToolBar()
        for eachToolData in self.toolData():
            if eachToolData[0]:
                item = toolbar.AddTool(eachToolData[0],
                                       eachToolData[1],
                                       shortHelpString=eachToolData[2])
                self.parent.Bind(wx.EVT_TOOL, eachToolData[3], item)
            else:
                toolbar.AddSeparator()

        toolbar.Realize()

    # 打开文件
    def OnOpenFile(self, event):
        pass

    # 保存
    def OnSave(self, event):
        pass

    # 保存全部
    def OnSaveAll(self, event):
        pass

    # 剪切
    def OnCut(self, event):
        pass

    # 复制
    def OnCopy(self, event):
        pass

    # 粘贴
    def OnPaste(self, event):
        pass

    # 撤销
    def OnUndo(self, event):
        pass

    # 重做
    def OnRedo(self, event):
        pass

    # 加粗
    def OnBold(self, event):
        pass

    # 斜体
    def OnItalic(self, event):
        pass

    # 下划线
    def OnUnderline(self, event):
        pass

    # 左对齐
    def OnAlignLeft(self, event):
        pass

    # 居中
    def OnALignCentre(self, event):
        pass

    # 右对齐
    def OnAlignRight(self, event):
        pass

    # 字体
    def OnFont(self, event):
        pass

    # 颜色
    def OnColour(self, event):
        pass
