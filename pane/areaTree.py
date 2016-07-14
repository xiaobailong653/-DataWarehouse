# -*- coding:utf8 -*-
#################################################
# Create By : sunlf
#
# Create On : 2016-07-02
#
# Comment : DataWarehouse
#################################################

import wx

from menus.menuStroage import MenuStorage
from utils.decorators import singleton


@singleton
class TreeCtrlHandler(wx.TreeCtrl):
    def __init__(self, parent, *args, **kw):
        style = wx.TR_HIDE_ROOT | wx.TR_HAS_BUTTONS
        wx.TreeCtrl.__init__(self, parent,
                             size=(200, 600),
                             style=style,
                             *args, **kw)
        self.root = None
        self.treeDom = None
        self.initBind()
        self.GetSelection
        self.GetItemParent

    def setRootItem(self, treeName):
        rootData = wx.TreeItemData(treeName)
        self.root = self.AddRoot(treeName, data=rootData)

    def setTreeDom(self, dom):
        self.treeDom = dom

    def getTreeDom(self):
        return self.treeDom

    def initBind(self):
        self.Parent.Bind(wx.EVT_TREE_SEL_CHANGED, self.OnSelChanged)
        self.Parent.Bind(wx.EVT_TREE_BEGIN_LABEL_EDIT, self.OnBeginLabelEdit)
        self.Parent.Bind(wx.EVT_TREE_END_LABEL_EDIT, self.OnEndLabelEdit)
        self.Parent.Bind(wx.EVT_TREE_DELETE_ITEM, self.OnDeleteItem)
        self.Parent.Bind(wx.EVT_TREE_ITEM_ACTIVATED, self.OnItemActivated)
        self.Parent.Bind(wx.EVT_TREE_ITEM_EXPANDED, self.OnItemExpanded)
        self.Parent.Bind(wx.EVT_TREE_ITEM_RIGHT_CLICK, self.OnItemRight)
        self.Parent.Bind(wx.EVT_TREE_ITEM_MENU, self.OnItemMenu)

    def loadData(self, farther, data):
        for item in data:
            treeItem = wx.TreeItemData(item['name'])
            treeItem.SetData(item['instance'])
            self.AppendItem(self.root, item['name'], data=treeItem)
            self.loadData(treeItem, item['child'])

    def insertItemNode(self, currentItem, itemType):
        text = u"新建节点"
        treeItem = wx.TreeItemData(text)
        if itemType == 'child':
            treeItem = wx.TreeItemData(text)
            treeItemId = self.AppendItem(currentItem, text, data=treeItem)
            self.Expand(currentItem)
        elif itemType == 'before':
            parentItem = self.GetItemParent(currentItem)
            index = self.getItemIndex(currentItem)
            treeItemId = self.InsertItemBefore(parentItem, index, text, data=treeItem)
        else:
            parentItem = self.GetItemParent(currentItem)
            treeItemId = self.InsertItem(parentItem, currentItem, text, data=treeItem)

        self.SelectItem(treeItemId)
        self.EditLabel(treeItemId)

    def OnSelChanged(self, event):
        pass

    def OnBeginLabelEdit(self, event):
        pass

    def OnEndLabelEdit(self, event):
        pass

    def OnDeleteItem(self, event):
        pass

    def OnItemActivated(self, event):
        pass

    def OnItemExpanded(self, event):
        pass

    def OnItemRight(self, event):
        item = event.GetItem()
        self.SelectItem(item, select=True)
        menu = MenuStorage(self.Parent)
        menu.createMenuItem()
        self.PopupMenu(menu)
        event.Skip()

    def OnItemMenu(self, event):
        pass
