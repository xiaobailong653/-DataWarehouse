# -*- coding:utf8 -*-
#################################################
# Create By : sunlf
#
# Create On : 2016-07-02
#
# Comment : DataWarehouse
#################################################

import wx


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
        self.SelectItem(item, select=True)  # 设置选中的Item
        menuData = self.menuCFData()
        self.menu = self.createMenu(menuData)
        self.PopupMenu(self.menu)
        event.Skip()

    def OnItemMenu(self, event):
        pass

    def createMenu(self, menuData):
        menu = wx.Menu()
        for eachItem in menuData:
            if eachItem[0]:
                item = menu.Append(-1, eachItem[0], eachItem[1])
                self.parent.Bind(wx.EVT_MENU, eachItem[2], item)
            else:
                menu.AppendSeparator()

        return menu

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

    def OnAddChildNode(self, event):
        pass

    def OnAddBefNode(self, event):
        pass

    def OnAddAftNode(self, event):
        pass

    def OnCut(self, event):
        pass

    def OnCopy(self, event):
        pass

    def OnPaste(self, event):
        pass

    def OnDelNode(self, event):
        pass

    def OnMoveUp(self, event):
        pass

    def OnMoveDown(self, event):
        pass

    def OnMoveLeft(self, event):
        pass

    def OnMoveRight(self, event):
        pass

    def OnRefresh(self, event):
        pass
