# -*- coding:utf8 -*-
#################################################
# Create By : sunlf
#
# Create On : 2016-06-29
#
# Comment : DataWarehouse
#################################################

from baseMenu import BaseMenu

class MenuEdit(BaseMenu):
    __menuName__ = "&编辑"

    def __init__(self, parent, *args, **kw):
        super(MenuEdit, self).__init__(parent, *args, **kw)
        self.parent = parent

    def menuItemData(self):
        return (('&切换编辑', u'切换编辑模式', self.OnChangeEdit),
                '',
                ('&撤销', u'撤销上次操作', self.OnUndo),
                ('&重做', u'重做刚才撤销的操作', self.OnRedo),
                '',
                ('&剪切', u'剪切选择内容到剪切板', self.OnCut),
                ('&复制', u'复制选择内容到剪切板', self.OnCopy),
                ('&粘贴', u'插入剪切板的内容到当前位置', self.OnPaste),
                '',
                ('&全选', u'选中全部的内容或节点', self.OnSelect),
                ('&反选', u'反选列表中所选的项目', self.OnTurnSelect),
                '',
                ('&删除', u'删除所选的内容或节点', self.OnDelete),
                '',
                ('&插入', u'插入指定的项目', self.OnInsert),)

    # 切换编辑模式
    def OnChangeEdit(self, event):
        pass

    # 撤销
    def OnUndo(self, event):
        pass

    # 重做
    def OnRedo(self, event):
        pass

    # 剪切
    def OnCut(self, event):
        pass

    # 复制
    def OnCopy(self, event):
        pass

    # 粘贴
    def OnPaste(self, event):
        pass

    # 全选
    def OnSelect(self, event):
        pass

    # 反选
    def OnTurnSelect(self, event):
        pass

    # 删除
    def OnDelete(self, event):
        pass

    # 插入
    def OnInsert(self, event):
        pass
