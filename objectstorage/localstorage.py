#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
Created on 2014年2月7日

@author: sunlongfei
'''
import os


class LocalStorage():

    def __init__(self, path):
        self.path = path

    def listdir(self):
        files = os.listdir(self.path)
        for f in files:
            print os.stat(self.path + '\\' + f)

if __name__ == "__main__":
    local = LocalStorage('D:\DriversBackup')
    local.listdir()
