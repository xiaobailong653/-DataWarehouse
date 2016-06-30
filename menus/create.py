#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
Created on 2014年1月10日

@author: sunlongfei
'''
################################################################
#
# 创建菜单栏
#
################################################################
import wx

from menus.responsefile import ResponseFile
from menus.responseedit import ResponseEdit
from menus.responsestorage import ResponseStorage
from menus.responsefind import ResponseFind
from menus.responseimport import ResponseImport
from menus.responseexport import ResponseExport
from menus.responseformat import ResponseFormat
from menus.responseparagraph import ResponseParagraph
from menus.responsetools import ResponseTools
from menus.responsewindow import ResponseWindow
from menus.responsehelp import ResponseHelp
from menus.responseconnect import ResponseConnect

# 创建菜单栏


class CreateMenu():

    def __init__(self, parent):
        self.parent = parent
        self.createMenuBar()

    # 为‘文件’菜单中增加项目
    def menuFile(self):
        res = ResponseFile(self.parent)
        return ('&文件', (
            ('&创建数据仓库', u'创建一个新的数据仓库', res.OnNew),
            ('&打开数据仓库', u'打开一个已经存在的数据仓库', res.OnOpen),
            ('', '', ''),
            ('&保存', u'保存更改到当前的数据仓库', res.OnSave),
            ('&保存全部', u'保存全部的更改到所有打开的数据仓库', res.OnSaveAll),
            ('', '', ''),
            ('&关闭', u'关闭当前打开的数据仓库', res.OnClose),
            ('&关闭全部', u'关闭所有打开的数据仓库', res.OnCloseAll),
            ('', '', ''),
            ('&打印设置', u'选择打印机，保存打印属性', res.OnSetPrinter),
            ('&打印预览', u'打印预览', res.OnPrinterPreview),
            ('&打印', u'打印文档', res.OnPrinter),
            ('', '', ''),
            ('&退出', u'退出数据仓库', res.OnCloseWindow)))

    # 为‘编辑’菜单中增加项目
    def menuEdit(self):
        res = ResponseEdit(self.parent)
        return ('&编辑', (
            ('&切换编辑', u'切换编辑模式', res.OnChangeEdit),
            ('', '', ''),
            ('&撤销', u'撤销上次操作', res.OnUndo),
            ('&重做', u'重做刚才撤销的操作', res.OnRedo),
            ('', '', ''),
            ('&剪切', u'剪切选择内容到剪切板', res.OnCut),
            ('&复制', u'复制选择内容到剪切板', res.OnCopy),
            ('&粘贴', u'插入剪切板的内容到当前位置', res.OnPaste),
            ('', '', ''),
            ('&全选', u'选中全部的内容或节点', res.OnSelect),
            ('&反选', u'反选列表中所选的项目', res.OnTurnSelect),
            ('', '', ''),
            ('&删除', u'删除所选的内容或节点', res.OnDelete),
            ('', '', ''),
            ('&插入', u'插入指定的项目', res.OnInsert),
        ))

    # 为‘仓库’菜单中增加项目
    def menuStorage(self):
        res = ResponseStorage(self.parent)
        return ('&仓库', (
            ('&添加子节点', u'在当前节点下增加子节点', res.OnAddChildNode),
            ('&向前插入节点', u'在当前节点前面插入节点', res.OnAddBefNode),
            ('&向后插入节点', u'在当前节点后面插入节点', res.OnAddAftNode),
            ('', '', ''),
            ('&剪切节点', u'剪切当前节点', res.OnCut),
            ('&复制节点', u'复制当前节点', res.OnCopy),
            ('&粘贴节点', u'粘贴节点成为当前节点的子节点', res.OnPaste),
            ('', '', ''),
            ('&删除节点', u'删除当前节点', res.OnDelNode),
            ('', '', ''),
            ('&节点上移', u'在当前节点下增加子节点', res.OnMoveUp),
            ('&节点下移', u'在当前节点下增加子节点', res.OnMoveDown),
            ('&节点左移', u'在当前节点下增加子节点', res.OnMoveLeft),
            ('&节点右移', u'在当前节点下增加子节点', res.OnMoveRight),
        ))

    def menuContent(self):
        res = ResponseConnect(self.parent)
        return ('&连接', (
            ('&S3存储', u'连接到S3存储', res.OnConnectS3),
            ('&阿里云存储', u'连接到阿里云存储', res.OnConnectAliyun),
            ('&SWIFT存储', u'连接到SWIFT存储', res.OnConnectSwift),
        ))

    # 为‘导入’菜单增加项目
    def menuImport(self):
        res = ResponseImport(self.parent)
        return ('&导入', (
            ('&导入', u'导入文件', res.OnImport),
        ))

    # 为‘导出’菜单增加项目
    def menuExport(self):
        res = ResponseExport(self.parent)
        return ('&导出', (
            ('&导出', u'导出文件', res.OnExport),
        ))

    # 为‘查找’菜单增加项目
    def menuFind(self):
        res = ResponseFind(self.parent)
        return ('&查找', (
            ('&查找', u'查找指定的内容', res.OnFind),
            ('&查找上一个', u'查找上一个内容', res.OnFindLast),
            ('&查找下一个', u'查找下一个内容', res.OnFindNext),
            ('', '', ''),
            ('&替换', u'替换查找到的内容', res.OnReplace),
        ))

    # 为‘格式’菜单增加项目
    def menuFormat(self):
        res = ResponseFormat(self.parent)
        return ('&格式', (
            ('&字体设置', u'设置字体属性', res.OnFont),
            ('', '', ''),
            ('&加粗', u'设置字体为加粗', res.OnFontBold),
            ('&斜体', u'设置字体为斜体', res.OnFontItalic),
            ('&下划线', u'为字体增加下划线', res.OnFontUnderline),
            ('&删除线', u'为字体增加删除线', res.OnFontDeleteline),
            ('', '', ''),
            ('&字体颜色', u'设置字体颜色', res.OnFontColour),
            ('&背景颜色', u'设置背景颜色', res.OnBackgroudColour),
            ('', '', ''),
            ('&高亮显示', u'文本高亮度显示', res.OnHighLight),
            ('', '', ''),
            ('&编辑链接', u'添加或编辑超级链接', res.OnEditHyperlink),
            ('&取消链接', u'取消超级链接', res.OnDeleteHyperlink),
        ))

    # 为‘段落’菜单增加项目
    def menuParagraph(self):
        res = ResponseParagraph(self.parent)
        return ('&段落', (
            ('&左对齐', u'左对齐', res.OnLeftAlign),
            ('&右对齐', u'右对齐', res.OnRightAlign),
            ('&居中', u'居中', res.OnMiddle),
            ('&两端对齐', u'两端对齐', res.OnTwoEndsAlign),
            ('', '', ''),
            ('&增加缩进', u'增加缩进', res.OnAddIndentation),
            ('&减少缩进', u'减少缩进', res.OnReduceIndentation),
            ('&自定义缩进', u'自定义缩进', res.OnCustomIndentation),
            ('', '', ''),
            ('&1倍行间距', u'1倍行间距', res.OnOneLineSpace),
            ('&1.5倍行间距', u'1.5倍行间距', res.OnOneHalfLineSpace),
            ('&2倍行间距', u'2倍行间距', res.OnTwoLineSpace),
            ('', '', ''),
            ('&段落间距', u'段落间距', res.OnParagraphSpace),
        ))

    def menuTools(self):
        res = ResponseTools(self.parent)
        return ('&工具', (
            ('&JSON格式化显示', u'JSON格式化显示', res.OnDisplayJson),
            ('&显示设置', u'显示设置', res.OnDisplaySetting),
        ))

    # 为‘窗口’菜单增加项目
    def menuWindow(self):
        res = ResponseWindow(self.parent)
        return ('&窗口', (
            ('&新窗口', u'打开新窗口', res.OnOpenWindow),
            ('', '', ''),
            ('&关闭当前窗口', u'关闭当前窗口', res.OnCloseWindow),
            ('&关闭所有子窗口', u'关闭所有子窗口', res.OnCloseAllWindows),
            ('', '', ''),
            ('&层叠排列', u'层叠排列窗口', res.OnStackWindows),
            ('&水平排列', u'水平排列窗口', res.OnHorizontalWindows),
            ('&垂直排列', u'垂直排列窗口', res.OnVerticalWindows),
            ('', '', ''),
            ('&排列图标', u'排列图标', res.OnArrangeIcon),
            ('', '', ''),
            ('&当前打开的窗口', u'切换到该窗口', res.OnChangeWindow),
        ))

    # 为‘帮助’菜单增加项目
    def menuHelp(self):
        res = ResponseHelp(self.parent)
        return ('&帮助', (
            ('&使用说明', u'使用说明', res.OnHelpContents),
            ('', '', ''),
            ('&检查更新', u'检查更新', res.OnUpdate),
            ('&技术支持', u'技术支持', res.OnSupport),
            ('&常见问题解答', u'常见问题解答', res.OnQuestion),
            ('', '', ''),
            ('&联系我们', u'联系我们', res.OnkContact),
            ('&产品注册', u'产品注册', res.OnRegister),
            ('', '', ''),
            ('&关于', u'关于数据仓库', res.OnAbout),
        ))

    # 增加所有的菜单项
    def menuDate(self):
        return (self.menuFile(),
                self.menuEdit(),
                self.menuStorage(),
                self.menuContent(),
                self.menuFind(),
                self.menuImport(),
                self.menuExport(),
                self.menuFormat(),
                self.menuParagraph(),
                self.menuTools(),
                self.menuWindow(),
                self.menuHelp())

    # 创建菜单栏
    def createMenuBar(self):
        menuBar = wx.MenuBar()
        for eachMenuData in self.menuDate():
            menuLabel = eachMenuData[0]
            menuItems = eachMenuData[1]
            menuBar.Append(self.createMenu(menuItems), menuLabel)

        self.parent.SetMenuBar(menuBar)

    # 创建单个菜单项
    def createMenu(self, menuData):
        menu = wx.Menu()
        for eachItem in menuData:
            if len(eachItem) == 2:
                label = eachItem[0]
                subMenu = self.createMenu(eachItem[1])
                menu.AppendMenu(wx.NewId(), label, subMenu)
            else:
                self.createMenuItem(menu, *eachItem)

        return menu

    # 为菜单项中增加项目
    def createMenuItem(self, menu, label, status, handler, kind=wx.ITEM_NORMAL):
        if not label:
            menu.AppendSeparator()
            return
        menuItem = menu.Append(-1, label, status, kind)  # 使用kind创建菜单项
        self.parent.Bind(wx.EVT_MENU, handler, menuItem)
