# -*- coding:utf8 -*-
#################################################
# Create By : sunlf
#
# Create On : 2016-06-29
#
# Comment : DataWarehouse
#################################################

import wx
import os
from menus.printer import PrintWork
from windows.dialog import DialogWindows
from dmanage.complexfile import ComplexFile
from dmanage.warehouse import WarehouseHandler
from dmanage.config import *
from baseMenu import BaseMenu
###############################################################
DS = 10000
DS_CREATE = DS + 1
DS_OPEN = DS + 2
###############################################################
wildcard = "DataStorage (*.slf)|*.slf|"\
           "All files (*.*)|*.*"
###############################################################


class MenuFile(BaseMenu):
    __menuName__ = "&文件"

    def __init__(self, parent, *args, **kw):
        super(MenuFile, self).__init__(parent, *args, **kw)
        self.parent = parent

    def menuItemData(self):
        return (('&创建数据仓库', u'创建一个新的数据仓库', self.OnNew),
                ('&打开数据仓库', u'打开一个已经存在的数据仓库', self.OnOpen),
                '',
                ('&保存', u'保存更改到当前的数据仓库', self.OnSave),
                ('&保存全部', u'保存全部的更改到所有打开的数据仓库', self.OnSaveAll),
                '',
                ('&关闭', u'关闭当前打开的数据仓库', self.OnClose),
                ('&关闭全部', u'关闭所有打开的数据仓库', self.OnCloseAll),
                '',
                ('&打印设置', u'选择打印机，保存打印属性', self.OnSetPrinter),
                ('&打印预览', u'打印预览', self.OnPrinterPreview),
                ('&打印', u'打印文档', self.OnPrinter),
                '',
                ('&退出', u'退出数据仓库', self.OnCloseWindow))

    # 新建数据仓库
    def OnNew(self, event):
        dlg = wx.FileDialog(self.parent,
                            u"新建数据仓库",
                            wildcard=wildcard,
                            style=wx.SAVE)
        if dlg.ShowModal() == wx.ID_OK:
            path = dlg.GetPath().encode('utf-8')
            if path:
                self._create_warehouse(path)
        dlg.Destroy()

    def _create_warehouse(self, path):
        warehouse = WarehouseHandler(path)
        warehouse.create()
        warehouse.save()

    # 打开数据仓库
    def OnOpen(self, event):
        dlg = wx.FileDialog(self.parent,
                            "打开数据仓库",
                            wildcard=wildcard,
                            style=wx.OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            path = dlg.GetPath()
            if path:
                self._show_data_storage(path, DS_OPEN)
        dlg.Destroy()

    def _open_warehouse(self, path):
        warehouse = WarehouseHandler(path)
        treeData = warehouse.getAllNodes()


    # 保存更改到数据仓库
    def OnSave(self, event):
        print '保存数据仓库'

    # 保存所有的更改到数据仓库
    def OnSaveAll(self, event):
        cf_tree = self.parent.getCFTreeHandle()
        cf_tree.saveToFile()

    # 关闭当前的数据仓库
    def OnClose(self, event):
        notebook = self.parent.getNotebookHandle()
        current_page = notebook.GetCurrentPage()
        if current_page is not None:
            page_idx = notebook.GetPageIndex(current_page)
            notebook.DeletePage(page_idx)

    # 关闭全部打开的数据仓库
    def OnCloseAll(self, event):
        print 'OnOpen'

    # 打印设置
    def OnSetPrinter(self, event):
        self.printer.printSetup()

    # 打印预览
    def OnPrinterPreview(self, event):
        import os
        filename = os.path.join(os.path.dirname(__file__), 'sample.txt')
        text = open(filename).read()
        result = self.printer.printPreview(text)
        if not result:
            self.dlg.error_message('打印预览', '打印预览失败！')

    # 打印
    def OnPrinter(self, event):
        text = 'hello'
        self.printer.printing(text)

    # 退出窗口
    def OnCloseWindow(self, event):
        self.parent.Close()
