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


class TreeCtrlHandler(wx.TreeCtrl):
    def __init__(self, parent, treeName, *args, **kw):
        super(TreeCtrlHandler, self).__init__(parent,
                                              size=(200, 600),
                                              *args, **kw)
        self.parent = parent
        rootData = wx.TreeItemData(treeName)
        self.root = self.AddRoot(treeName, data=rootData)
        data = wx.TreeItemData("first")
        self.AppendItem(self.root, "first", data=data)
        self.initBind()

    def initBind(self):
        self.parent.Bind(wx.EVT_TREE_SEL_CHANGED, self.OnSelChanged)
        self.parent.Bind(wx.EVT_TREE_BEGIN_LABEL_EDIT, self.OnBeginLabelEdit)
        self.parent.Bind(wx.EVT_TREE_END_LABEL_EDIT, self.OnEndLabelEdit)
        self.parent.Bind(wx.EVT_TREE_DELETE_ITEM, self.OnDeleteItem)
        self.parent.Bind(wx.EVT_TREE_ITEM_ACTIVATED, self.OnItemActivated)
        self.parent.Bind(wx.EVT_TREE_ITEM_EXPANDED, self.OnItemExpanded)
        self.parent.Bind(wx.EVT_TREE_ITEM_RIGHT_CLICK, self.OnItemRight)
        self.parent.Bind(wx.EVT_TREE_ITEM_MENU, self.OnItemMenu)

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
        menu = MenuStorage(self.parent)
        menu.createMenuItem()
        self.PopupMenu(menu)
        event.Skip()

    def OnItemMenu(self, event):
        pass
