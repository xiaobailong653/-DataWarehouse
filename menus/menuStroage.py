# -*- coding:utf8 -*-
#################################################
# Create By : sunlf
#
# Create On : 2016-06-29
#
# Comment : DataWarehouse
#################################################

from baseMenu import BaseMenu
from eventId import (
    ID_AddChildNode,
    ID_AddBefNode,
    ID_AddAftNode,
    ID_CutNode,
    ID_CopyNode,
    ID_PasteNode,
    ID_DeleteNode,
    ID_MoveUpNode,
    ID_MoveDownNode,
    ID_MoveLeftNode,
    ID_MoveRightNode,
    ID_NodeAttribute,)


class MenuStorage(BaseMenu):
    __menuName__ = "&仓库"

    def __init__(self, parent, *args, **kw):
        super(MenuStorage, self).__init__(parent, *args, **kw)
        self.parent = parent

    def menuItemData(self):
        return (('&添加子节点', u'在当前节点下增加子节点', ID_AddChildNode),
                ('&向前插入节点', u'在当前节点前面插入节点', ID_AddBefNode),
                ('&向后插入节点', u'在当前节点后面插入节点', ID_AddAftNode),
                '',
                ('&剪切节点', u'剪切当前节点', ID_CutNode),
                ('&复制节点', u'复制当前节点', ID_CopyNode),
                ('&粘贴节点', u'粘贴节点成为当前节点的子节点', ID_PasteNode),
                '',
                ('&删除节点', u'删除当前节点', ID_DeleteNode),
                '',
                ('&节点上移', u'在当前节点下增加子节点', ID_MoveUpNode),
                ('&节点下移', u'在当前节点下增加子节点', ID_MoveDownNode),
                ('&节点左移', u'在当前节点下增加子节点', ID_MoveLeftNode),
                ('&节点右移', u'在当前节点下增加子节点', ID_MoveRightNode),
                '',
                ('&属性', u'节点属性', ID_NodeAttribute))

    def bindData(self):
        return ((self.OnAddChildNode, ID_AddChildNode),
                (self.OnAddBefNode, ID_AddBefNode),
                (self.OnAddAftNode, ID_AddAftNode),
                (self.OnCutNode, ID_CutNode),
                (self.OnCopyNode, ID_CopyNode),
                (self.OnPasteNode, ID_PasteNode),
                (self.OnDelNode, ID_DeleteNode),
                (self.OnMoveUp, ID_MoveUpNode),
                (self.OnMoveDown, ID_MoveDownNode),
                (self.OnMoveLeft, ID_MoveLeftNode),
                (self.OnMoveRight, ID_MoveRightNode),
                (self.OnNodeAttribute, ID_NodeAttribute),)

    def _insertNode(self, nodeType):
        leftTree = self.parent.leftTree
        treeItemId = leftTree.GetSelection()
        print dir(treeItemId)
        leftTree.insertItemNode(treeItemId, nodeType)

    # 插入子节点
    def OnAddChildNode(self, event):
        self._insertNode("child")

    # 向前插入节点
    def OnAddBefNode(self, event):
        self._insertNode("before")

    # 向后插入节点
    def OnAddAftNode(self, event):
        self._insertNode("after")

    # 剪切节点
    def OnCutNode(self, event):
        print "this is OnCut"

    # 复制节点
    def OnCopyNode(self, event):
        print "this is OnCopy"

    # 粘贴节点
    def OnPasteNode(self, event):
        print "this is OnPaste"

    # 删除节点
    def OnDelNode(self, event):
        print "this is OnDelNode"

    # 节点上移
    def OnMoveUp(self, event):
        print "this is OnMoveUp"

    # 节点下移
    def OnMoveDown(self, event):
        print "this is OnMoveDown"

    # 节点左移
    def OnMoveLeft(self, event):
        print "this is OnMoveLeft"

    # 节点右移
    def OnMoveRight(self, event):
        print "this is OnMoveRight"

    # 节点右移
    def OnNodeAttribute(self, event):
        print "this is OnNodeAttribute"
