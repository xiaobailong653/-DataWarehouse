#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
Created on 2014年3月1日

@author: sunlongfei
'''
import os

import wx


class Bitmap():

    def __init__(self):
        img_save_all = wx.Image('images/save_all.png', wx.BITMAP_TYPE_ANY)

    def imgToBitmap(self, name):
        img = wx.Image(name, wx.BITMAP_TYPE_ANY)
        img.Scale(24, 24)

    def getBitmap(self, name):
        img = self.imgToBitmap(name)
        return wx.BitmapFromImage(img)
