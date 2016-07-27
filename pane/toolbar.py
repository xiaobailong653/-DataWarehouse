# -*- coding:utf8 -*-
#################################################
# Create By : sunlf
#
# Create On : 2016-07-14
#
# Comment : DataWarehouse
#################################################

import wx
import wx.lib.agw.aui as aui

from utils.decorators import singleton
from eventId import (
    ID_NewDataWarehouse,
    ID_OpenDataWarehouse,
    ID_SavePage)

# @singleton
class ToolbarHandler(aui.AuiToolBar):
    def __init__(self, parent, *args, **kw):
        aui.AuiToolBar.__init__(self, parent)
        self.initToorbar()

    def initToorbar(self):
        self.SetToolBitmapSize(wx.Size(16, 16))
        tb3_bmp1 = wx.ArtProvider.GetBitmap(wx.ART_FOLDER, wx.ART_OTHER, wx.Size(16, 16))
        self.AddSimpleTool(ID_NewDataWarehouse, u"新建", tb3_bmp1)
        self.AddSimpleTool(ID_OpenDataWarehouse, u"打开", tb3_bmp1)
        self.AddSimpleTool(ID_SavePage, u"保存", tb3_bmp1)
        self.AddSeparator()
