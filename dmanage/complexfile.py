#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
Created on 2014年2月14日

@author: sunlongfei
'''
import os
import zipfile
import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom
from datetime import datetime


class ComplexFile():

    def __init__(self):
        self.attrib = {'create': '2013-02-17', 'update': ''}

    # 判断是否是有效的数据仓库文件
    def isCF(self, handle):
        try:
            if handle.find('./title/name') is not None:
                return True
            else:
                return False
        except:
            return False

    # 创建数据仓库文件
    def createCF(self, filename):
        complexfile = ET.Element('complexfile')
        title = ET.SubElement(complexfile, 'title', self.attrib)
        name = ET.SubElement(title, 'name')
        name.text = filename
        body = ET.SubElement(complexfile, 'body')
        self.stream_add(body, '增加新节点...', '')
        ET.ElementTree(complexfile).write(filename, encoding='utf-8')

    def test(self, handle):
        body = handle.find('.//body')
        if body is not None:
            for i in range(0, 5):
                name = 'item-%s' % i
                value = 'this is %s' % name
                farther = self.stream_add(body, name, value)
                for j in range(0, 4):
                    name = 'item-%s-%s' % (i, j)
                    value = 'this is %s' % name
                    child_j = self.stream_add(farther, name, value)
                    for k in range(0, 3):
                        name = 'item-%s-%s-%s' % (i, j, k)
                        value = 'this is %s' % name
                        self.stream_add(child_j, name, value)

    # 迭代获取文件名字信息
    def iterBody(self, streams):
        items = []
        if streams is not None:
            for stream in streams:
                name = stream.find('./name')
                if name is not None:
                    stream_child = stream.findall('./stream')
                    if stream_child:
                        item = [name.text]
                        item.append(self.iterBody(stream))
                        items.append(item)
                    else:
                        items.append(name.text)
        return items

#     def get_stream(self, handle, name):
#         streams = handle.findall('.//stream')
#         for stream in streams:
#             node_name = stream.find('./name')
#             if node_name is not None and node_name.text == name:
#                 return stream
#
#         return None

    # 添加流文件
    def stream_add(self, farther, name, value):
        stream = ET.SubElement(farther, 'stream', self.attrib)
        streamname = ET.SubElement(stream, 'name')
        streamname.text = name
        streamvalue = ET.SubElement(stream, 'value')
        streamvalue.text = value

        return stream

    # 重命名流文件
    def stream_rename(self, handle, src_name, dst_name):
        stream = self.get_stream(handle, src_name)
        if stream is not None:
            stream.find('./name').text = dst_name
            return True

        return False

    def stream_move(self, handle, path):
        return self.get_stream_handle(handle, path)

    def stream_paste(self, src_stream, dst_stream, flag):
        if src_stream is not None and dst_stream is not None:
            copy_stream = src_stream.copy()
            dst_stream.append(copy_stream)
            if flag:
                src_stream.clear()

    # 删除流文件
    def stream_del(self, handle, name):
        stream = self.get_child_form_farther(handle, name)
        if stream is not None and handle is not None:
            handle.remove(stream)

    def stream_update(self, stream, name='', value='', attrib={}):
        if name:
            stream.find('./name').text = name
        if value:
            stream.find('./value').text = value

    # 打开数据仓库文件
    def openCF(self, filename):
        self.etree = ET.parse(filename)
        root = self.etree.getroot()

        return root

    # 获取流文件的名字
    def get_stream_name(self, stream):
        if stream is not None:
            return stream.find('./name').text
        return None

    # 获取流文件的内容
    def get_stream_value(self, stream):
        if stream is not None:
            return stream.find('./value').text
        return None

    # 获取流文件的属性
    def get_stream_attrib(self, stream):
        if stream is not None:
            return stream.attrib

        return None

    # 获取存储部分的句柄
    def get_body_handle(self, root):
        return root.find('.//body')

    # 从父节点中获取子节点
    def get_child_form_farther(self, farther, child_name):
        if farther is not None:
            streams = farther.findall('./stream')
            for stream in streams:
                text = stream.find('./name').text
                if text == child_name:
                    return stream

        return None

    # 根据路径获取流文件句柄
    def get_stream_handle(self, handle, path):
        items = path.split('/')
        for item in items:
            if item:
                handle = self.get_child_form_farther(handle, item)

        return handle

    # 获取流文件树
    def get_all_streams(self, handle):
        if handle is not None:
            streams = handle.findall('./stream')
            items = self.iterBody(streams)
            return items
        else:
            return None

    # 将流文件树保存到文件中
    def save(self, handle, outfile):
        ET.ElementTree(handle).write(outfile, encoding='utf-8')

    def display(self, node):
        '''显示xml内容'''
        data = ET.tostring(node, 'utf-8')
        reparsed = minidom.parseString(data)
        dis = reparsed.toprettyxml(encoding='utf-8')
        print dis

if __name__ == "__main__":
    cf = ComplexFile()
    filename = "D://mydatabase/datastorage/exmple.slf"
    cf.createCF(filename)
    cf_handle = cf.openCF(filename)
    cf.test(cf_handle)
    body = cf.get_body_handle(cf_handle)
    stream = cf.get_stream_handle(body, '/item-4/item-4-0')
    body.append(stream)
    cf.display(body)
#     name = 'item-1-1'
#     rename = 'test-1-1'
#     body = cf.get_body_handle(cf_handle)
#     #cf.stream_rename(body, name, rename)
#     cf.stream_del(body, rename)
    cf.save(cf_handle, filename)
#     body = cf.get_body_handle(cf_handle)
#     stream = cf.get_stream_handle(body, '/')
#     print cf.get_stream_name(stream)
#     print cf.get_stream_value(stream)
#     print cf.get_stream_attrib(stream)
#     print cf.get_stream_father_handle(stream)
#
