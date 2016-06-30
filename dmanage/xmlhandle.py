#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
Created on 2014年2月17日

@author: sunlongfei
'''
import xml.etree.ElementTree as ET
from datetime import datetime


class XmlHandle():

    def __init__(self):
        pass

    def add_node(self, tag, attrib={}):
        if tag:
            return ET.Element(tag, attrib)
        else:
            return None

    def add_chile_node(self, parent, child, attrib={}, text=None):
        '''为指定节点增加孩子节点（节点名称，属性， 值）'''
        node = ET.SubElement(parent, child, attrib)
        if text:
            node.text = text

        return node

    def read(self, srcfile):
        if srcfile:
            return ET.parse(srcfile)
        else:
            return None

    def get_root(self, handle):
        '''获取根节点'''
        return handle.getroot()

    def get_path_text(self, handle, path):
        '''根据path获取节点的值'''
        node = handle.find(path)
        try:
            return node.text
        except:
            return node

    def get_path_properties(self, handle, path):
        '''根据path获取节点的属性'''
        node = handle.find(path)
        try:
            return node.attrib
        except:
            return node

    def find_node(self, handle, path):
        '''根据path获取节点'''
        return handle.find(path)

    def find_nodes(self, handle, path):
        '''根据path获取节点列表'''
        return handle.findall(path)

    def write(self, root, outfile):
        if root is not None:
            ET.ElementTree(root).write(outfile, encoding='utf-8')
            return True
        else:
            return False

if __name__ == "__main__":
    xh = XmlHandle()
#     root = xh.add_node('root1')
#     xh.add_chile_node(root, "child1", {"create":'now'})
#     xh.write(root, "test.xml")
    el = ET.ElementTree(file='text.xml')
