# -*- coding:utf8 -*-
#################################################
# Create By : sunlf
#
# Create On : 2016-06-29
#
# Comment : DataWarehouse
#################################################
import codecs
import os.path
from xml.dom import minidom
from datetime import datetime

# from utils.decorators import lazy_property


class WarehouseHandler(object):
    def __init__(self, filePath):
        self.filePath = filePath

    # @lazy_property
    def getDomName(self):
        return os.path.basename(self.filePath)

    def create(self):
        dom = minidom.getDOMImplementation()
        self.doc = dom.createDocument(None, "warehouse", None)
        root = self.doc.documentElement
        domName = self.getDomName()
        root.setAttribute("name", domName)
        root.setAttribute("create", datetime.today().isoformat())
        treeNode = self.doc.createElement('richtext')
        treeNode.setAttribute("name", u"请在此创建节点")
        treeNode.setAttribute("create", datetime.today().isoformat())
        treeNode.setAttribute("content", "url")
        root.appendChild(treeNode)

    def getAllNodes(self):
        self.doc = minidom.parse(self.filePath)
        root = self.doc.documentElement
        return self.parseDom(root)

    def parseDom(self, doc):
        dom = []
        for child in doc.childNodes:
            if child.nodeType == child.ELEMENT_NODE:
                data = {key: value for key, value in child.attributes.items()}
                data['child'] = self.parseDom(child)
                dom.append(data)
        return dom

    def save(self):
        fname = codecs.open(self.filePath, 'w', 'utf-8')
        self.doc.writexml(fname, addindent='  ', newl='\n', encoding='utf-8')
        fname.close()


if __name__ == '__main__':
    handler = WarehouseHandler("../other/other.xml")
    data = handler.getAllNodes()
    print data
