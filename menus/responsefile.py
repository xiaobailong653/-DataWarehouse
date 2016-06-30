#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
Created on 2014年1月10日

@author: sunlongfei
'''
################################################################
#
# 响应菜单栏中‘文件’标签的事件
#
################################################################

import wx
import os
from menus.printer import PrintWork
from windows.dialog import DialogWindows
from dmanage.complexfile import ComplexFile
from dmanage.config import *
###############################################################
DS = 10000
DS_CREATE = DS + 1
DS_OPEN = DS + 2
###############################################################
wildcard = "DataStorage (*.slf)|*.slf|"\
           "All files (*.*)|*.*"
###############################################################


def toutf8(data):
    d_list = []
    if type(data) == list:
        for l in data:
            d_list.append(l.encode('utf-8'))
    elif type(data) == unicode:
        return data.encode('utf-8')

    return d_list


class ResponseFile():

    def __init__(self, parent):
        self.parent = parent
        self.dlg = DialogWindows(self.parent)
        self.printer = PrintWork(self.parent)

    def _show_data_storage(self, path, flag=DS_CREATE):
        storage_name = os.path.basename(path)
        self.parent.cf_tree = self.parent.panes.addCFTree(storage_name,
                                                          storage_name,
                                                          path)
        update_option(self.parent.configfile,
                      'path', 'cf_defalt_path', path)

    def _create_data_storage(self, path):
        cf = ComplexFile()
        cf.createCF(path)
        self._show_data_storage(path)

    # 新建数据仓库
    def OnNew(self, event):
        dlg = wx.FileDialog(self.parent,
                            "新建数据仓库",
                            wildcard=wildcard,
                            style=wx.SAVE)
        if dlg.ShowModal() == wx.ID_OK:
            path = dlg.GetPath().encode('utf-8')
            if path:
                self._create_data_storage(path)
        dlg.Destroy()
        #path = "D://mydatabase/datastorage/test.xml"
        # self._show_data_storage(path)

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

#         path = "D://mydatabase/datastorage/test.xml"
#         self._show_data_storage(path, DS_OPEN)

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

if __name__ == '__main__':
    path = "c:\\datatim.txt"
    ex_name = os.path.splitext(path)
    print ex_name
    print path
