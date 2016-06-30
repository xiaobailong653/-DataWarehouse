#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
Created on 2013年12月17日

@author: sunlongfei
'''
import json
# import libxml2
# import oss.oss_api as osshandler


def xml_to_dict(root):
    '''xml字符串转化成字典'''
    xml_dict = {}
    for child in root.children:
        if 'element' == child.type:
            conunt = child.lsCountNode()
            if conunt < 2:
                xml_dict[child.name] = child.content
            else:
                xml_dict[child.name] = xml_to_dict(child)

    return xml_dict


def display_list(liebiao):
    d = []
    for i in range(len(liebiao)):
        d.append(liebiao[i])
        if i % 5 == 0:
            print d
            d = []

    print d


def display(content):
    print json.dumps(content, indent=1)


class Aliyun(object):

    def __init__(self, website='oss.aliyuncs.com',
                 ID='HB50JO83yRE8KhLG',
                 KEY='3fAiGQ4Cu4tDeq9rCXG72P1ITcInJa'):
        self.oss = osshandler.OssAPI(website, ID, KEY)

    def draw_error(self, status, content):
        '''分析错误，转换成字典形式的错误结果'''
        doc = libxml2.parseDoc(content)
        root = doc.children
        result = {'status': status}
        for child in root.children:
            if 'element' == child.type:
                result[child.name] = child.content

        return result

    def bucket_create(self, name, acl='private'):
        '''Bucket的三种权限（private，public-read，public-read-write）'''
        res = self.oss.create_bucket(name, acl)
        if 2 == res.status / 100:
            return True
        else:
            return self.draw_error(res.status, res.read())

    def bucket_delete(self, name):
        '''删除 bucket'''
        res = self.oss.delete_bucket(name)
        if 2 == res.status / 100:
            return True
        else:
            return self.draw_error(res.status, res.read())

    def bucket_update_acl(self, name, acl):
        '''修改bucket的权限， （private，public-read，public-read-write）'''
        res = self.oss.put_bucket(name, acl)
        if 2 == res.status / 100:
            return True
        else:
            return self.draw_error(res.status, res.read())

    def _get_acl(self, content):
        '''从xml中获取acl'''
        doc = libxml2.parseDoc(content)
        root = doc.children
        for child in root.children:
            if 'Grant' == child.name:
                return child.content

        return None

    def get_bucket_acl(self, name):
        '''获取bucket的权限'''
        res = self.oss.get_bucket_acl(name)
        if 2 == res.status / 100:
            return self._get_acl(res.read())
        else:
            return self.draw_error(res.status, res.read())

    def _get_buckets(self, content):
        '''从xml中获取bucket列表'''
        doc = libxml2.parseDoc(content)
        root = doc.children
        buckets = []
        for child in root.children:
            if 'Bucket' == child.name:
                bucket = xml_to_dict(child)
                buckets.append(bucket)

        return buckets

    def get_all_buckets(self):
        '''获取所有的bucket'''
        res = self.oss.list_all_my_buckets()
        if 2 == res.status / 100:
            return self._get_buckets(res.read())
        else:
            return self.draw_error(res.status, res.read())

    def upload_file(self, bucket, object_name, src_name):
        '''上传文件对象到bucket'''
        res = self.oss.put_object_from_file(bucket, object_name, src_name)
        if 2 == res.status / 100:
            return True
        else:
            return self.draw_error(res.status, res.read())

    def _get_objects(self, content):
        '''从xml中获取object列表'''
        doc = libxml2.parseDoc(content)
        root = doc.children
        objects = []
        for child in root.children:
            if 'Contents' == child.name:
                obs = xml_to_dict(child)
                objects.append(obs)

        return objects

    def get_bucket_objects(self, bucket):
        '''获取bucket下所有的object'''
        res = self.oss.get_bucket(bucket)
        if 2 == res.status / 100:
            return self._get_objects(res.read())
        else:
            return self.draw_error(res.status, res.read())

    def delete_file(self, bucket, object_name):
        '''删除bucket中的指定object'''
        res = self.oss.delete_object(bucket, object_name)
        if 2 == res.status / 100:
            return True
        else:
            return self.draw_error(res.status, res.read())

    def download_file(self, bucket, object_name, dst_name):
        '''下载object到本地'''
        res = self.oss.get_object_to_file(bucket, object_name, dst_name)
        if 2 == res.status / 100:
            return True
        else:
            return self.draw_error(res.status, res.read())


if __name__ == '__main__':
    aliyun = Aliyun()
    #res = aliyun.bucket_create('test', 'public-read')
    #res = aliyun.bucket_delete('sunlf')
    #res = aliyun.bucket_update_acl('sunl', 'public-read-write')
    #res = aliyun.get_bucket_acl('sunl')
    res = aliyun.get_all_buckets()
    #res = aliyun.upload_file('sunlf', 'test-01', 'text.txt')
    #res = aliyun.get_bucket_objects('sunlf')
    #res = aliyun._get_objects(content)
    #res = aliyun.delete_file('sunlf', 'test')
    display(res)
