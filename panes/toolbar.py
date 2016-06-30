#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
Created on 2014年1月23日

@author: sunlongfei
'''

import wx
from PIL import Image as images
import os
import wx.lib.agw.aui as aui
import wx.richtext as rt
from dmanage.textdata import TextData
from dmanage.complexfile import ComplexFile
from panes.textctrl import TextControl
from dmanage.config import *
########################################################
ID_CreateTree = wx.ID_HIGHEST + 1
ID_DropDownToolbarItem = ID_CreateTree + 41
TB = 90000
TB_OPEN = TB + 1
TB_SAVE = TB + 2
TB_SAVE_ALL = TB + 3
TB_CUT = TB + 4
TB_COPY = TB + 5
TB_PASTE = TB + 6
TB_UNDO = TB + 7
TB_REDO = TB + 8
TB_BOLD = TB + 9
TB_ITALIC = TB + 10
TB_UNDERLINE = TB + 11
TB_ALIGN_LEFT = TB + 12
TB_ALIGN_CENTRE = TB + 13
TB_ALIGN_RIGHT = TB + 14
TB_FONT = TB + 15
TB_COLOUR_FONT = TB + 16
TB_COLOUR_BACKGROUND = TB + 17
TB_COLOUR_RED = TB + 200
TB_COLOUR_BLACK = TB + 201
TB_COLOUR_WHITE = TB + 202
TB_COLOUR_YELLOW = TB + 203
TB_COLOUR_GREEN = TB + 204
TB_COLOUR_MORE = TB + 300
###############################################################
DS = 10000
DS_CREATE = DS + 1
DS_OPEN = DS + 2

###############################################################
wildcard = "DataStorage (*.slf)|*.slf|"\
           "All files (*.*)|*.*"
###############################################################


###############################################################
class ToolBar(aui.AuiToolBar):

    def __init__(self, parent):
        self.parent = parent

        aui.AuiToolBar.__init__(self, parent, -1, wx.DefaultPosition, wx.DefaultSize,
                                agwStyle=aui.AUI_TB_DEFAULT_STYLE | aui.AUI_TB_OVERFLOW)
        self.SetToolBitmapSize(wx.Size(16, 16))

    def initToolBar(self):
        tools = [self.createBaseTool,
                 self.createCheckTool,
                 self.createFontTool,
                 self.createColourTool,
                 self.createSearchTool]

        for tool in tools:
            tool()

        self.Realize()

    def bitmap(self, name):
        img = wx.Image(name, wx.BITMAP_TYPE_ANY)
        icon = img.Scale(16, 16)
        icon_bitmap = wx.BitmapFromImage(icon)

        return icon_bitmap
    # 工具栏的数据

    def baseToolData(self):

        return ((-1, '打开', self.bitmap('images/save.png'), self.OnOpenFile, ''),
                ('', '', '', ''),
                (-1, '保存', self.bitmap('images/save.png'), self.OnSave, ''),
                (-1, '保存全部', self.bitmap('images/save_all.png'), self.OnSaveAll, ''),
                ('', '', '', ''),
                (wx.ID_CUT, '剪切', self.bitmap('images/save.png'), self.OnCut, self.OnCut),
                (wx.ID_COPY, '复制', self.bitmap('images/save.png'), self.OnCopy, self.OnCopy),
                (wx.ID_PASTE, '粘贴', self.bitmap('images/save.png'), self.OnPaste, self.OnPaste),
                (wx.ID_DELETE, '删除', self.bitmap('images/delete.png'), self.OnDelete, ''),
                ('', '', '', ''),
                (wx.ID_UNDO, '撤销', self.bitmap('images/save.png'), self.OnUndo, self.OnUndo),
                (wx.ID_REDO, '重做', self.bitmap('images/save.png'), self.OnRedo, self.OnRedo),
                ('', '', '', ''),
                (-1, '左对齐', self.bitmap('images/save.png'), self.OnAlignLeft, ''),
                (-1, '居中', self.bitmap('images/save.png'), self.OnALignCentre, ''),
                (-1, '右对齐', self.bitmap('images/save.png'), self.OnAlignRight, ''),
                ('', '', '', ''),
                (-1, '减少缩进', self.bitmap('images/save.png'), self.OnIndentLess, ''),
                (-1, '增加缩进', self.bitmap('images/save.png'), self.OnIndentMore, ''),
                ('', '', '', ''),)

    # 创建工具栏

    def createBaseTool(self):
        def doBind(item, handler, updateUI):
            self.Bind(wx.EVT_TOOL, handler, item)
            if updateUI:
                self.Bind(wx.EVT_UPDATE_UI, updateUI, item)

        base_tool_data = self.baseToolData()
        for eachToolData in base_tool_data:
            if eachToolData[0]:
                simple_tool = self.AddSimpleTool(eachToolData[0],
                                                 eachToolData[1],
                                                 eachToolData[2],
                                                 eachToolData[1])
                doBind(simple_tool, eachToolData[3], eachToolData[4])
            else:
                self.AddSeparator()

    def checkToolData(self):
        return ((-1, '加粗', self.bitmap('images/save.png'),
                 self.OnBold, self.OnUpdateBold),
                (-1, '斜体', self.bitmap('images/save.png'),
                 self.OnItalic, ''),
                (-1, '下划线', self.bitmap('images/save.png'),
                 self.OnUnderline, ''),
                ('', '', ''),)

    def createCheckTool(self):
        def doBind(item, handler, updateUI):
            self.Bind(wx.EVT_TOOL, handler, item)
            if updateUI:
                self.Bind(wx.EVT_UPDATE_UI, updateUI, item)

        for eachToolData in self.checkToolData():
            if eachToolData[0]:
                check_tool = self.AddCheckTool(eachToolData[0],
                                               eachToolData[1],
                                               eachToolData[2],
                                               wx.NullBitmap,
                                               eachToolData[1])
                doBind(check_tool, eachToolData[3], eachToolData[4])
            else:
                self.AddSeparator()

    def createFontTool(self):
        enum = wx.FontEnumerator()
        enum.EnumerateFacenames()
        style_choices = enum.GetFacenames()
        style_choices.sort()
        font_style = wx.ComboBox(self, -1, "", choices=style_choices,
                                 size=(150, -1), style=wx.CB_DROPDOWN)
        self.AddControl(font_style, '字体')
        self.Bind(wx.EVT_COMBOBOX, self.OnFontFace, font_style)

        size_choices = ['8', '9', '10', '11', '12', '13',
                        '14', '15', '16', '17', '18', '19',
                        '20', '24', '28', '30', '32', '64']
        font_size = wx.ComboBox(self, -1, "", choices=size_choices,
                                size=(50, -1), style=wx.CB_DROPDOWN)
        self.AddControl(font_size, '字体大小')
        self.Bind(wx.EVT_COMBOBOX, self.OnFontSize, font_size)

        self.AddSeparator()

    def createColourTool(self):
        self.AddSimpleTool(TB_COLOUR_FONT, "字体颜色", self.bitmap('images/fcolour.png'), '字体颜色')
        self.Bind(aui.EVT_AUITOOLBAR_TOOL_DROPDOWN, self.OnDropDownToolbarItem,
                  id=TB_COLOUR_FONT)
        self.SetToolDropDown(TB_COLOUR_FONT, True)
        self.AddSimpleTool(TB_COLOUR_BACKGROUND, "背景颜色", self.bitmap('images/save.png'), '背景颜色')
        self.Bind(aui.EVT_AUITOOLBAR_TOOL_DROPDOWN, self.OnDropDownToolbarItem,
                  id=TB_COLOUR_BACKGROUND)
        self.SetToolDropDown(TB_COLOUR_BACKGROUND, True)
        self.AddSeparator()

    def createSearchTool(self):
        search = SearchCtrl(self, size=(150, -1), doSearch=self.DoSearch)
        self.AddControl(search)
        self.AddSeparator()

    def _show_data_storage(self, path, flag=DS_CREATE):
        storage_name = os.path.basename(path)
        pane = self.parent.getPaneHandle()
#         if pane.left_cf_tree is not None:
#             pane.closePaneItem()
        pane.left_cf_tree = pane.addCFTree(storage_name,
                                           path)
        update_option(self.parent.configfile,
                      'path', 'cf_defalt_path', path)

    # 打开文件

    def OnOpenFile(self, event):
        dlg = wx.FileDialog(self.parent,
                            "新建数据仓库",
                            wildcard=wildcard,
                            style=wx.OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            path = dlg.GetPath().encode('utf-8')
            if path:
                self._show_data_storage(path)
        dlg.Destroy()

    # 保存

    def OnSave(self, event):
        pass

    # 保存全部
    def OnSaveAll(self, event):
        cf_tree = self.parent.getCFTreeHandle()
        cf_tree.saveToFile()

    # 获取当前选择的page
    def getCurrentPage(self):
        notebook = self.parent.getNotebookHandle()
        page_idx = notebook.GetSelection()
        if page_idx != -1:
            page = notebook.GetPage(page_idx)
            return page
        return ''

    def ForwardEvent(self, event):
        page = self.getCurrentPage()
        if page:
            page.ProcessEvent(event)

    # 剪切
    def OnCut(self, event):
        self.ForwardEvent(event)

    # 复制
    def OnCopy(self, event):
        self.ForwardEvent(event)

    # 粘贴
    def OnPaste(self, event):
        self.ForwardEvent(event)

    # 删除
    def OnDelete(self, event):
        page = self.getCurrentPage()
        if page:
            start, end = page.GetSelection()
            page.Remove(start, end)

    # 撤销
    def OnUndo(self, event):
        self.ForwardEvent(event)

    # 重做
    def OnRedo(self, event):
        self.ForwardEvent(event)

#     def OnUpdateBold(self, event):
#         page = self.getCurrentPage()
#         print "updatebold"
#         if page:
#             print "updatebold"
#             event.Check(page.isSelectionBold())

    # 加粗
    def OnBold(self, event):
        page = self.getCurrentPage()
        if page:
            start, end = page.GetSelection()
            font = page.GetFont()
            if event.IsChecked():
                font.SetWeight(wx.BOLD)
            else:
                font.SetWeight(wx.NORMAL)

            attr = wx.TextAttr(font=font)
            page.SetStyle(start, end, attr)

        event.Skip()

    # 斜体
    def OnItalic(self, event):
        page = self.getCurrentPage()
        if page:
            start, end = page.GetSelection()
            font = page.GetFont()
            if event.IsChecked():
                font.SetStyle(wx.ITALIC)
            else:
                font.SetStyle(wx.NORMAL)
            attr = wx.TextAttr(font=font)
            page.SetStyle(start, end, attr)

    # 下划线
    def OnUnderline(self, event):
        page = self.getCurrentPage()
        if page:
            start, end = page.GetSelection()
            font = page.GetFont()
            font.SetUnderlined(True)
            attr = wx.TextAttr(font=font)
            page.SetStyle(start, end, attr)

    # 删除线
    def OnDeleteline(self, event):
        page = self.getCurrentPage()
        if page:
            start, end = page.GetSelection()
            font = page.GetFont()
            # font
            attr = wx.TextAttr(font=font)
            page.SetStyle(start, end, attr)

    # 左对齐
    def OnAlignLeft(self, event):
        page = self.getCurrentPage()
        if page:
            start, end = page.GetSelection()
            attr = wx.TextAttr(alignment=wx.TEXT_ALIGNMENT_LEFT)
            page.SetStyle(start, end, attr)

    # 居中
    def OnALignCentre(self, event):
        page = self.getCurrentPage()
        if page:
            start, end = page.GetSelection()
            attr = wx.TextAttr(alignment=wx.TEXT_ALIGNMENT_CENTRE)
            page.SetStyle(start, end, attr)

    # 右对齐
    def OnAlignRight(self, event):
        page = self.getCurrentPage()
        if page:
            start, end = page.GetSelection()
            attr = wx.TextAttr(alignment=wx.TEXT_ALIGNMENT_RIGHT)
            page.SetStyle(start, end, attr)

    # 减少缩进
    def OnIndentLess(self, event):
        page = self.getCurrentPage()
        if page:
            attr = wx.TextAttr()
            attr.SetFlags(wx.TEXT_ATTR_LEFT_INDENT)
            ip = page.GetInsertionPoint()
            if page.GetStyle(ip, attr):
                start, end = page.GetSelection()

            if attr.GetLeftIndent() >= 100:
                attr.SetLeftIndent(attr.GetLeftIndent() - 100)
            else:
                attr.SetLeftIndent(0)
            attr.SetFlags(wx.TEXT_ATTR_LEFT_INDENT)
            page.SetStyle(start, end, attr)

    # 增加缩进
    def OnIndentMore(self, event):
        page = self.getCurrentPage()
        if page:
            attr = wx.TextAttr()
            attr.SetFlags(wx.TEXT_ATTR_LEFT_INDENT)
            ip = page.GetInsertionPoint()
            if page.GetStyle(ip, attr):
                start, end = page.GetSelection()
                attr.SetLeftIndent(attr.GetLeftIndent() + 100)
                attr.SetFlags(wx.TEXT_ATTR_LEFT_INDENT)
                page.SetStyle(start, end, attr)

    def DoSearch(self):
        pass

    def colourMenuData(self):
        return ((TB_COLOUR_RED, '红色', ''),
                (TB_COLOUR_BLACK, '黑色', ''),
                (TB_COLOUR_WHITE, '白色', ''),
                (TB_COLOUR_YELLOW, '黄色', ''),
                (TB_COLOUR_GREEN, '绿色', ''),
                ('', '', ),
                (TB_COLOUR_MORE, '更多颜色...', ''))

    def colourMenu(self):
        menuPopup = wx.Menu()
        menuData = self.colourMenuData()
        for colourItem in menuData:
            if colourItem[0]:
                bmp = wx.ArtProvider.GetBitmap(wx.ART_HELP, wx.ART_OTHER, wx.Size(16, 16))
                menuItem = wx.MenuItem(menuPopup, -1, colourItem[1])
                self.Bind(wx.EVT_MENU, self.OnSetColour, menuItem)
                menuItem.SetBitmap(bmp)
                menuPopup.AppendItem(menuItem)
            else:
                menuPopup.AppendSeparator()

        return menuPopup

    def OnSetColour(self, event):
        print event.GetInt()
        pass

    def OnDropDownToolbarItem(self, event):
        if event.IsDropDownClicked():

            tb = event.GetEventObject()
            tb.SetToolSticky(event.GetId(), True)

            # create the popup menu
            menuPopup = self.colourMenu()

            # line up our menu with the button
            rect = tb.GetToolRect(event.GetId())
            pt = tb.ClientToScreen(rect.GetBottomLeft())
            pt = self.ScreenToClient(pt)

            self.PopupMenu(menuPopup, pt)

            # make sure the button is "un-stuck"
            tb.SetToolSticky(event.GetId(), False)

    def OnFontFace(self, event):
        page = self.getCurrentPage()
        if page:
            facename = event.GetString()
            start, end = page.GetSelection()
            fontData = wx.FontData()
            fontData.EnableEffects(False)
            font = fontData.GetChosenFont()
            font.SetFaceName(facename)
            attr = wx.TextAttr(font=font)
            page.SetStyle(start, end, attr)

    def OnFontSize(self, event):
        print event.GetString()

    # 加粗
    def OnUpdateBold(self, event):
        pass

    # 斜体
    def OnUpdateItalic(self, event):
        pass
    # 下划线

    def OnUpdateUnderline(self, event):
        pass

    def OnUpdateDeleteline(self, event):
        pass

    # 左对齐
    def OnUpdateAlignLeft(self, event):
        page = self.getCurrentPage()
        if page:
            pass

    # 居中
    def OnUpdateALignCentre(self, event):
        page = self.getCurrentPage()
        if page:
            pass

    # 右对齐
    def OnUpdateAlignRight(self, event):
        page = self.getCurrentPage()
        if page:
            pass


class SearchCtrl(wx.SearchCtrl):
    maxSearches = 5

    def __init__(self, parent, id=-1, value="",
                 pos=wx.DefaultPosition, size=wx.DefaultSize, style=0,
                 doSearch=None):
        style |= wx.TE_PROCESS_ENTER
        wx.SearchCtrl.__init__(self, parent, id, value, pos, size, style)
        self.Bind(wx.EVT_TEXT_ENTER, self.OnTextEntered)
        self.Bind(wx.EVT_MENU_RANGE, self.OnMenuItem, id=1, id2=self.maxSearches)
        self.doSearch = doSearch
        self.searches = []

    def OnTextEntered(self, evt):
        text = self.GetValue()
        if self.doSearch(text):
            self.searches.append(text)
            if len(self.searches) > self.maxSearches:
                del self.searches[0]
            self.SetMenu(self.MakeMenu())
        self.SetValue("")

    def OnMenuItem(self, evt):
        text = self.searches[evt.GetId()-1]
        self.doSearch(text)

    def MakeMenu(self):
        menu = wx.Menu()
        item = menu.Append(-1, "Recent Searches")
        item.Enable(False)
        for idx, txt in enumerate(self.searches):
            menu.Append(1+idx, txt)
        return menu
