# -*- coding:utf8 -*-
#################################################
# Create By : sunlf
#
# Create On : 2016-06-29
#
# Comment : DataWarehouse
#################################################


import wx


class DataWarehouseFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1,
                          u"数据仓库",
                          size=(1024, 600),
                          pos=(50, 50))


if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = DataWarehouseFrame()
    frame.Show()
    app.MainLoop()
