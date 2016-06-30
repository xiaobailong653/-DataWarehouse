# -*- coding:utf8 -*-
#################################################
# Create By : sunlf
#
# Create On : 2016-06-29
#
# Comment : DataWarehouse
#################################################

import wx


class BaseMenu(wx.Menu):
    __menuName__ = ""

    def __init__(self, parent, *args, **kw):
        super(BaseMenu, self).__init__(*args, **kw)
        self.parent = parent

    def menuItemData(self):
        return ()

    def createMenuItem(self):
        for menuItem in self.menuItemData():
            if menuItem:
                item = self.Append(wx.NewId(), menuItem[0], menuItem[1], wx.ITEM_NORMAL)
                self.parent.Bind(wx.EVT_MENU, menuItem[2], item)
            else:
                self.AppendSeparator()
