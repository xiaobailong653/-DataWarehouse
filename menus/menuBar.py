# -*- coding:utf8 -*-
#################################################
# Create By : sunlf
#
# Create On : 2016-06-29
#
# Comment : DataWarehouse
#################################################


import wx

from menuFile import MenuFile
from menuEdit import MenuEdit
from menuStroage import MenuStorage


class MenuBarHandler(wx.MenuBar):
    def __init__(self, parent, *args, **kw):
        super(MenuBarHandler, self).__init__(*args, **kw)
        self.parent = parent
        self.initBar()

    def initBar(self):
        for menu in self.menuObjects():
            menuObject = menu(self.parent)
            menuObject.createMenuItem()
            self.Append(menuObject, menuObject.__menuName__)
            menuObject.bindEvents()

    def menuObjects(self):
        return (MenuFile,
                MenuEdit,
                MenuStorage,)
