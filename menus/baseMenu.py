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

    def bindData(self):
        return ()

    def createMenuItem(self):
        for menuItem in self.menuItemData():
            if menuItem:
                if isinstance(menuItem[2], int):
                    self.Append(menuItem[2], menuItem[0], menuItem[1])
                else:
                    item = self.Append(-1, menuItem[0], menuItem[1], wx.ITEM_NORMAL)
                    self.parent.Bind(wx.EVT_MENU, menuItem[2], item)
            else:
                self.AppendSeparator()

    def bindEvents(self):
        for item in self.bindData():
            self.parent.Bind(wx.EVT_MENU, item[0], id=item[1])
