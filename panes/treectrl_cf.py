#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
Created on 2014年1月21日

@author: sunlongfei
'''
import wx
import os.path
import wx.richtext as richtext
from dmanage.textdata import TextData
from panes.textctrl import RichTextCtrl, TextControl
from dmanage.complexfile import ComplexFile


class CFTree(wx.TreeCtrl):

    def __init__(self, parent, filename=None):
        self.parent = parent
        self.filename = filename
        self.update_flag = True
        self.cc_item = None
        self.cc_flag = True  # 剪切为True，复制为False

        style = wx.TR_DEFAULT_STYLE | wx.NO_BORDER | wx.TR_HIDE_ROOT
        style = style | wx.TR_EDIT_LABELS
        wx.TreeCtrl.__init__(self, parent, -1, wx.Point(0, 0), (200, 250),
                             style)
        self.iconsInit()
        self.buildEvt()
        if filename is not None:
            self.cf = ComplexFile()
            self.handle = self.cf.openCF(filename)
            tree_name = os.path.basename(filename)
            self.init(self.handle, tree_name)

    def init(self, handle, tree_name):
        self.body = self.cf.get_body_handle(handle)
        streams = self.cf.get_all_streams(self.body)
        self.root = self.addRootNode(tree_name)
        self.addTreeNodes(self.root, streams)

    def iconsInit(self):
        icons = wx.ImageList(16, 16)
        self.fldridx = icons.Add(wx.ArtProvider.GetBitmap(wx.ART_FOLDER, wx.ART_OTHER, (16, 16)))
        self.fldropenidx = icons.Add(wx.ArtProvider.GetBitmap(wx.ART_NORMAL_FILE, wx.ART_OTHER, (16, 16)))
        self.fileidx = icons.Add(wx.ArtProvider.GetBitmap(wx.ART_NORMAL_FILE, wx.ART_OTHER, (16, 16)))
        self.AssignImageList(icons)

    def buildEvt(self):
        self.Bind(wx.EVT_TREE_ITEM_RIGHT_CLICK, self.OnRightClick)
        self.Bind(wx.EVT_TREE_ITEM_ACTIVATED, self.OnActivated)
        self.Bind(wx.EVT_TREE_SEL_CHANGED, self.OnSelChanged)
        self.Bind(wx.EVT_TREE_BEGIN_LABEL_EDIT, self.OnBeginLabelEdit)
        self.Bind(wx.EVT_TREE_END_LABEL_EDIT, self.OnEndLabelEdit)

    def addRootNode(self, name):
        root = self.AddRoot(name)
        self.SetItemImage(root, self.fldridx, wx.TreeItemIcon_Normal)  # 设置根图像
        self.SetItemImage(root, self.fldropenidx, wx.TreeItemIcon_Expanded)

        return root

    def addTreeNodes(self, parentItem, items):
        if type(items) == list:
            for item in items:
                if type(item) == list:
                    newItem = self.AppendItem(parentItem, item[0])
                    self.SetItemImage(newItem, self.fldridx, wx.TreeItemIcon_Normal)
                    self.SetItemImage(newItem, self.fldropenidx, wx.TreeItemIcon_Expanded)
                    self.addTreeNodes(newItem, item[1])
                else:
                    newItem = self.AppendItem(parentItem, item)
                    self.SetItemImage(newItem, self.fileidx, wx.TreeItemIcon_Normal)
        else:
            newItem = self.AppendItem(parentItem, items)
            self.SetItemImage(newItem, self.fileidx, wx.TreeItemIcon_Normal)

        # self.Expand(parentItem)

    def menuCFData(self):
        return (('&添加子节点', '在当前节点下增加子节点', self.OnAddChildNode),
                ('&向前插入节点', '在当前节点前面插入节点', self.OnAddBefNode),
                ('&向后插入节点', '在当前节点后面插入节点', self.OnAddAftNode),
                ('', '', ''),
                ('&剪切', '剪切当前节点', self.OnCut),
                ('&复制', '复制当前节点', self.OnCopy),
                ('&粘贴', '粘贴节点成为当前节点的子节点', self.OnPaste),
                ('', '', ''),
                ('&删除', '删除当前节点', self.OnDelNode),
                ('', '', ''),
                ('&节点上移', '在当前节点下增加子节点', self.OnMoveUp),
                ('&节点下移', '在当前节点下增加子节点', self.OnMoveDown),
                ('&节点左移', '在当前节点下增加子节点', self.OnMoveLeft),
                ('&节点右移', '在当前节点下增加子节点', self.OnMoveRight),
                ('', '', ''),
                ('&刷新', '刷新', self.OnRefresh),)

    def createMenu(self, menuData):
        menu = wx.Menu()
        for eachItem in menuData:
            if eachItem[0]:
                item = menu.Append(-1, eachItem[0], eachItem[1])
                self.parent.Bind(wx.EVT_MENU, eachItem[2], item)
            else:
                menu.AppendSeparator()

        return menu

    # 获取节点文本
    def getItemText(self, item):
        if item:
            return self.GetItemText(item)
        else:
            return ''

    # 获取节点路径
    def getItemPath(self, item):
        if item is not None:
            if item == self.GetRootItem():
                return ''
            else:
                parent = self.GetItemParent(item)
                return self.getItemPath(parent) + '/' + self.getItemText(item)
        else:
            return ''

    # 响应’右键‘， 显示菜单栏
    def OnRightClick(self, event):
        item = event.GetItem()
        self.SelectItem(item, select=True)  # 设置选中的Item
        menuData = self.menuCFData()
        self.menu = self.createMenu(menuData)
        self.PopupMenu(self.menu)
        event.Skip()

    def _add_notebook_page(self, notebook, page, text, data, parent):
        count = notebook.GetPageCount()
        for i in range(0, count):
            page_text = notebook.GetPageText(i)
            if page_text == text:
                notebook.SetPageText(i, text+'123')
                text = text + '345'

        if data:
            page.write(data)
            notebook.AddPage(page, text, select=True)

    def _open_notebook_page(self, item):
        text = self.getItemText(item)
        path = self.getItemPath(item)
        notebook = self.parent.getNotebookHandle()
        page_count = notebook.GetPageCount()
        children = notebook.getChildrenNames()
        if path in children.keys():
            notebook.SetSelectionToWindow(children[path])
            return

        # 获取父节点
        def get_parent(path):
            items = path.split('/')
            if len(items) > 2:
                return items[-2]
            else:
                return ''

        for i in range(0, page_count):
            page_text = notebook.GetPageText(i)
            if page_text == text:
                page = notebook.GetPage(i)
                name = page.GetName()
                notebook.SetPageText(i, text+'(%s)' % get_parent(name))
                text = text + '(%s)' % get_parent(path)

        stream = self.cf.get_stream_handle(self.body, path)
        if stream is not None:
            data = self.cf.get_stream_value(stream)
            #new_page = RichTextCtrl(self.parent, path)
            new_page = TextControl(notebook, path)
            if data:
                new_page.WriteText(data)
            notebook.AddPage(new_page, text, select=True)

    def _open_richtext(self, item):
        text = self.getItemText(item)
        path = self.getItemPath(item)
        stream = self.cf.get_stream_handle(self.body, path)
        if stream is not None:
            data = self.cf.get_stream_value(stream)
            richtext = RichTextCtrl(self.parent, path)
            if data:
                richtext.WriteText(data)

    # 响应’双击‘事件
    def OnActivated(self, event):
        item = event.GetItem()
        self._open_richtext(item)

    # 响应’节点选择变更‘事件
    def OnSelChanged(self, event):
        self.current_item = event.GetItem()
        event.Skip()

    def _add_child_node(self, current_item, text, edit=True):
        count = self.GetChildrenCount(current_item)
        if count == 0:
            self.SetItemImage(self.current_item, self.fldridx, wx.TreeItemIcon_Normal)
            self.SetItemImage(self.current_item, self.fldropenidx, wx.TreeItemIcon_Expanded)
        newItem = self.AppendItem(current_item, text)
        self.SetItemImage(newItem, self.fileidx, wx.TreeItemIcon_Normal)
        self.Expand(self.current_item)
        if edit:
            self.EditLabel(newItem)
            self.update_flag = False

    # 增加子节点
    def OnAddChildNode(self, event):
        current_item = self.GetSelection()
        self._add_child_node(current_item, '增加新节点...')

    # 获取item的索引
    def getItemIndex(self, item):
        i = 0
        prev = self.GetPrevSibling(item)
        print
        while prev.IsOk():
            i = i + 1
            prev = self.GetPrevSibling(prev)

        return i

    # 向前插入节点
    def OnAddBefNode(self, event):
        current_item = self.GetSelection()
        farther = self.GetItemParent(current_item)
        index = self.getItemIndex(current_item)
        newItem = self.InsertItemBefore(farther, index, '增加新节点...')
        self.SetItemImage(newItem, self.fileidx, wx.TreeItemIcon_Normal)
        self.EditLabel(newItem)
        self.SelectItem(newItem, select=True)
        self.update_flag = False

    # 向后插入节点
    def OnAddAftNode(self, event):
        current_item = self.GetSelection()
        farther = self.GetItemParent(current_item)
        newItem = self.InsertItem(farther, current_item, '增加新节点...')
        self.SetItemImage(newItem, self.fileidx, wx.TreeItemIcon_Normal)
        self.EditLabel(newItem)
        self.SelectItem(newItem, select=True)
        self.update_flag = False

    # 剪切节点
    def OnCut(self, event):
        self.cc_item = self.GetSelection()
        self.cc_flag = True
        event.Skip()

    # 复制节点
    def OnCopy(self, event):
        self.cc_item = self.GetSelection()
        self.cc_flag = False
        event.Skip()

    def _paste(self, src_stream, dst_stream, flag=True):
        self.cf.stream_paste(src_stream, dst_stream, flag)

    # 粘贴节点
    def OnPaste(self, event):
        current_item = self.GetSelection()
        if self.cc_item is not None:
            text = self.getItemText(self.cc_item)
            src_path = self.getItemPath(self.cc_item)
            dst_path = self.getItemPath(current_item)
            src_stream = self.cf.get_stream_handle(self.body, src_path)
            dst_stream = self.cf.get_stream_handle(self.body, dst_path)
            streams = self.cf.get_all_streams(src_stream)
            if streams:
                items = [[text, streams]]
            else:
                items = [text]
            self.addTreeNodes(current_item, items)
            if self.cc_flag:
                self._del_node(self.cc_item)
                self._paste(src_stream, dst_stream)
            else:
                self._paste(src_stream, dst_stream, False)

        self.Expand(current_item)

    def _cf_delete(self, farther_path, del_name):
        farther = self.cf.get_stream_handle(self.body, farther_path)
        self.cf.stream_del(farther, del_name)
        # self.saveToFile()

    def _del_node(self, current_item):
        farther = self.GetItemParent(current_item)
        farther_path = self.getItemPath(farther)
        self._cf_delete(farther_path, self.getItemText(current_item))
        self.Delete(current_item)

    # 删除当前节点及子节点
    def OnDelNode(self, event):
        current_item = self.GetSelection()
        self._del_node(current_item)

    # 向上移动节点
    def OnMoveUp(self, event):
        print 'OnActivated'

    # 向下移动节点
    def OnMoveDown(self, event):
        print 'OnActivated'

    # 左移动节点成为父节点
    def OnMoveLeft(self, event):
        print 'OnActivated'

    # 右移动节点成为子节点
    def OnMoveRight(self, event):
        print 'OnActivated'

    # 节点标签开始变更
    def OnBeginLabelEdit(self, event):
        self.b_label = event.GetLabel()
        self.update_flag = True

    # 更新节点
    def _update_label_name(self, item):
        name = self.getItemText(item)
        path = self.getItemPath(item)
        stream = self.cf.get_stream_handle(self.body, path)
        if stream is None:
            farter = self.GetItemParent(item)
            far_path = self.getItemPath(farter)
            far_stream = self.cf.get_stream_handle(self.body, far_path)
            self.cf.stream_add(far_stream, name, '')
            self._open_notebook_page(item)
        else:
            if self.update_flag:
                self.cf.stream_update(stream, name)
            else:
                print '%s 已经存在！' % name
                self.EditLabel(item)
        # self.saveToFile()

    # 节点变更完成
    def OnEndLabelEdit(self, event):
        item = event.GetItem()
        self.e_label = event.GetLabel()
        if self.e_label:
            self.SetItemText(item, self.e_label)

        self._update_label_name(item)

    def OnRefresh(self, event):
        streams = self.cf.get_all_streams(self.body)
        self.DeleteAllItems()
        self.addTreeNodes(self.root, streams)
        event.Skip()

    def saveToFile(self):
        self.cf.save(self.handle, self.filename)
