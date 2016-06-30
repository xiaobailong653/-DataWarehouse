#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
Created on 2014年1月23日

@author: sunlongfei
'''
import os

#from win32com.client import Dispatch, constants
import ctypes
from ctypes import *

STGM_WRITE = 0x00000001
STGM_CREATE = 0x00001000
STGM_SHARE_EXCLUSIVE = 0x00000010


class TextData():

    def __init__(self, filename):
        self.fname = filename

    def fwrite(self, data):
        open(self.fname, 'w').write(data)

    def fread(self):
        '''以gbk编码读取（当然是读取gbk编码格式的文字了）并忽略错误的编码，转换成utf-8编码输出 '''
        return open(self.fname, 'r').read().decode('unicode', 'ignore').encode('utf-8')

# class CompositeFiles():
#     def __init__(self):
#         word = Dispatch('Word.Application')
#         word.Visible = 0
#         word.DisplayAlerts = 0
#         #doc = word.Documents.Open(FileName='test.doc')
#         word.Documents.Add('test.doc')
#         #myrange = doc.Range(0, 0)
#         #myrange.InsertBefore('Hell from Python')
#         #word.Documents.Close(word.wdDoNotSaveChanges)
#         #word.Quit()
#
# def cf():
#     cf = ctypes.cdll.LoadLibrary('cf')
#     #storage = cf.GetIStorage()
#     wcFilename = ctypes.c_wchar_p()
#     wcFilename.value = "D://mydatabase/datastorage/python-test.stg"
#     wcStorage = ctypes.c_wchar_p()
#     wcStorage.value = "storage"
#     storage = cf.CFCreateFile(wcFilename)
#     if storage:
#         for i in range(0, 4):
#             wcStorage = ctypes.c_wchar_p()
#             wcStorage.value = "storage%s"%i
#             storage = cf.CFCreateStorage(ctypes.c_void_p(storage), wcStorage)
#             if storage:
#                 cf.CFCreateStream(storage, ctypes.c_wchar_p("stream"))
#     else:
#         print "false"
#
# if __name__ == '__main__':
#     from win32com import olectl
#     print dir(olectl)
#
