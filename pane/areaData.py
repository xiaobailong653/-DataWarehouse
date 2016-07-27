# -*- coding:utf8 -*-
#################################################
# Create By : sunlf
#
# Create On : 2016-07-05
#
# Comment : DataWarehouse
#################################################

import wx.richtext


class RichTextHandler(wx.richtext.RichTextCtrl):
    def __init__(self, parent):
        style = wx.TE_MULTILINE | wx.NO_BORDER
        super(RichTextHandler, self).__init__(parent, -1,
                                              style=style,
                                              name="areaData")
