#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
Created on 2014年1月8日

@author: sunlongfei
'''

import wx

# 标准的打印框架
FONTSIZE = 10


class TextDocPrintout(wx.Printout):

    def __init__(self, text, title, margins):
        wx.Printout.__init__(self, title)
        self.lines = text.split('\n')
        self.margins = margins

    def HasPage(self, page):
        return page <= self.numPages

    def GetPageInfo(self):
        return (1, self.numPages, 1, self.numPages)

    def CalculateScale(self, dc):
        ppiPrinterX, ppiPrinterY = self.GetPPIPrinter()
        ppiScreenX, ppiScreenY = self.GetPPIScreen()
        logScale = float(ppiPrinterX)/float(ppiScreenX)
        pw, ph = self.GetPageSizePixels()
        dw, dh = dc.GetSize()
        scale = logScale*float(dw)/float(pw)
        dc.SetUserScale(scale, scale)
        self.logUnitsMM = float(ppiPrinterX)/(logScale*25.4)

    def CalculateLayout(self, dc):
        topLeft, bottomRight = self.margins
        dw, dh = dc.GetSize()
        self.x1 = topLeft.x * self.logUnitsMM
        self.y1 = topLeft.y * self.logUnitsMM
        self.x2 = dc.DeviceToLogicalXRel(dw) - bottomRight.x * self.logUnitsMM
        self.y2 = dc.DeviceToLogicalXRel(dh) - bottomRight.y * self.logUnitsMM
        self.pageHeight = self.y2 - self.y1 - 2*self.logUnitsMM
        font = wx.Font(FONTSIZE, wx.TELETYPE, wx.NORMAL, wx.NORMAL)
        dc.SetFont(font)
        self.lineHeight = dc.GetCharHeight()
        self.linesPerPage = int(self.pageHeight/self.lineHeight)

    def OnPreparePrinting(self):
        dc = self.GetDC()
        self.CalculateScale(dc)
        self.CalculateLayout(dc)
        self.numPages = len(self.lines) / self.linesPerPage
        if len(self.lines) % self.linesPerPage != 0:
            self.numPages += 1

    def OnPrintPage(self, page):
        dc = self.GetDC()
        self.CalculateScale(dc)
        self.CalculateLayout(dc)
        dc.SetPen(wx.Pen('black', 0))
        dc.SetBrush(wx.TRANSPARENT_BRUSH)
        r = wx.RectPP((self.x1, self.y1), (self.x2, self.y2))
        dc.DrawRectangleRect(r)
        dc.SetClippingRect(r)
        line = (page-1)*self.linesPerPage
        x = self.x1 + self.logUnitsMM
        y = self.y1 + self.logUnitsMM
        while line < (page * self.linesPerPage):
            dc.DrawText(self.lines[line], x, y)
            y += self.lineHeight
            line += 1
            if line >= len(self.lines):
                break

        return True


class PrintWork():

    def __init__(self, parent):
        self.parent = parent

        self.pdata = wx.PrintData()
        self.pdata.SetPaperId(wx.PAPER_LETTER)
        self.pdata.SetOrientation(wx.PORTRAIT)

        self.margins = (wx.Point(15, 15), wx.Point(15, 15))

    def pageSetup(self):
        data = wx.PageSetupDialogData()
        data.SetPrintData(self.pdata)
        data.SetDefaultMinMargins(True)
        data.SetMarginTopLeft(self.margins[0])
        data.SetMarginBottomRight(self.margins[1])
        dlg = wx.PageSetupDialog(self, data)
        if dlg.ShowModal() == wx.ID_OK:
            data = dlg.GetPageSetupData()
            self.pdata = wx.PrintData(data.GetPrintData())
            self.pdata.SetPaperId(data.GetPaperId())
            self.margins = (data.GetMarginTopLeft(), data.GetMarginBottomRight())
        dlg.Destroy()

    # 打印设置
    def printSetup(self):
        data = wx.PrintDialogData(self.pdata)
        dlg = wx.PrintDialog(self.parent, data)
        dlg.GetPrintDialogData()
        result = dlg.ShowModal()
        data = dlg.GetPrintDialogData()
        self.pdata = wx.PrintData(data.GetPrintData())
        dlg.Destroy()

    # 打印预览
    def printPreview(self, text):
        data = wx.PrintDialogData(self.pdata)
        printout1 = TextDocPrintout(text, '打印预览', self.margins)
        printout2 = None
        preview = wx.PrintPreview(printout1, printout2, data)
        if not preview.Ok():
            return False
        else:
            frame = wx.PreviewFrame(preview, self.parent, '打印预览',
                                    pos=self.parent.GetPosition(),
                                    size=self.parent.GetSize())
            frame.Initialize()
            frame.Show()

        return True

    # 打印
    def printing(self, text):
        data = wx.PrintDialogData(self.pdata)
        printer = wx.Printer(data)
        printout = TextDocPrintout(text, '', self.margins)
        useSetupDialog = True
        if not printer.Print(self.parent, printout, useSetupDialog)and printer.GetLastError() == wx.PRINTER_ERROR:
            return False
        else:
            data = printer.GetPrintDialogData()
            self.pdata = wx.PrintData(data.GetPrintData())
        printout.Destroy()
        return True
