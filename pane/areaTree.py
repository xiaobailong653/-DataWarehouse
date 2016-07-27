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
from dmanage.warehouse import WarehouseHandler


@singleton
class TreeCtrlHandler(wx.TreeCtrl):
    def __init__(self, parent, *args, **kw):
        style = wx.TR_HIDE_ROOT | wx.TR_HAS_BUTTONS | wx.TR_EDIT_LABELS | wx.TR_LINES_AT_ROOT
        wx.TreeCtrl.__init__(self, parent,
                             size=(200, 600),
                             style=style,
                             *args, **kw)
        self.root = None
        self.treeDom = None
        self.initBind()
        self.initImageList()
        self.initData()

    def initData(self):
        path = "other/other.xml"
        warehouse = WarehouseHandler(path)
        treeData = warehouse.getAllNodes()
        domName = warehouse.getDomName()
        self.DeleteAllItems()
        self.setRootItem(domName)
        self.setTreeDom(warehouse)
        self.loadData(self.root, treeData)

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

    def initImageList(self):
        imageSize = (16, 16)
        imageList = wx.ImageList(*imageSize)
        self.fldridx = imageList.Add(wx.ArtProvider_GetBitmap(wx.ART_FOLDER, wx.ART_OTHER, imageSize))
        self.fldropenidx = imageList.Add(wx.ArtProvider_GetBitmap(wx.ART_FOLDER_OPEN, wx.ART_OTHER, imageSize))
        self.fileidx = imageList.Add(wx.ArtProvider_GetBitmap(wx.ART_NORMAL_FILE, wx.ART_OTHER, imageSize))
        self.AssignImageList(imageList)

    def loadData(self, farther, data):
        for item in data:
            treeItem = wx.TreeItemData(item['name'])
            treeItem.SetData(item['instance'])
            treeItemId = self.AppendItem(farther, item['name'], data=treeItem)
            self.SetItemImage(treeItemId, self.fldropenidx, wx.TreeItemIcon_Expanded)
            if item['child']:
                self.SetItemImage(treeItemId, self.fldridx, wx.TreeItemIcon_Normal)
                self.loadData(treeItemId, item['child'])
            else:
                self.SetItemImage(treeItemId, self.fileidx, wx.TreeItemIcon_Normal)

    def insertItemNode(self, currentItem, itemType):
        text = u"新建节点"
        treeItem = wx.TreeItemData(text)
        if itemType == 'child':
            treeItem = wx.TreeItemData(text)
            treeItemId = self.AppendItem(currentItem, text, self.fileidx, data=treeItem)
            self.Expand(currentItem)
        elif itemType == 'before':
            parentItem = self.GetItemParent(currentItem)
            prevItem = self.GetPrevSibling(currentItem)
            if prevItem.IsOk():
                treeItemId = self.InsertItem(parentItem, prevItem, text, self.fileidx, data=treeItem)
            else:
                treeItemId = self.PrependItem(parentItem, text, self.fileidx, data=treeItem)
        else:
            parentItem = self.GetItemParent(currentItem)
            treeItemId = self.InsertItem(parentItem, currentItem, text, self.fileidx, data=treeItem)

        self.SelectItem(treeItemId)
        self.EditLabel(treeItemId)

    def getItemIndex(self, item):
        i = 0
        prev = self.GetPrevSibling(item)
        while prev.IsOk():
            i = i + 1
            prev = self.GetPrevSibling(prev)

        return i

    def getTreePath(self, item):
        path = []
        path.append(self.getItemIndex(item))
        parent = self.GetItemParent(item)
        if parent != self.root:
            path += self.getTreePath(parent)
        return path

    def OnSelChanged(self, event):
        pass

    def OnBeginLabelEdit(self, event):
        pass

    def OnEndLabelEdit(self, event):
        path = self.getTreePath(event.Item)
        text = event.GetLabel()
        self.treeDom.addNodeByPath(path, text)

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
