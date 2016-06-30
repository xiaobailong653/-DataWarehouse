#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
Created on 2014年2月20日

@author: sunlongfei
'''
import ConfigParser
import json

# 把配置写入到文件


def write_config(filename, config):
    fname = open(filename, 'w')
    config.write(fname)
    fname.close()

# 创建配置文件


def create_configfile(filename, config_data):
    config = ConfigParser.ConfigParser()
    for section in config_data.keys():
        config.add_section(section)
        item = config_data[section]
        for option in item.keys():
            config.set(section, option, item[option])
    write_config(filename, config)

# 获取所有的管理


def get_sections(filename):
    data = {}
    config = ConfigParser.ConfigParser()
    fname = open(filename)
    config.readfp(fname, 'rb')
    for section in config.sections():
        options = config.items(section)
        for option in options:
            data[option[0]] = option[1]

    return data

# 获取子项目的值


def get_section_option(filename, section, options):
    config = ConfigParser.ConfigParser()
    config.read(filename)
    try:
        opt = config.get(section, options)
    except:
        return None

    return opt

# get appointed section


def get_section(filename, section, options):
    config = ConfigParser.ConfigParser()
    fname = open(filename)
    config.readfp(fname, 'rb')
    resource = {}
    if section in config.sections():
        for option in options:
            try:
                resource[option] = config.get(section, option)
            except ConfigParser.NoOptionError:
                pass

    return resource

# add section to config file


def add_section(filename, options, add_section):
    config = ConfigParser.ConfigParser()
    config.read(filename)
    for section in add_section.keys():
        config.add_section(section)
        item = add_section[section]
        for option in item.keys():
            config.set(section, option, item[option])

    config.write(open(filename, 'w'))

# delete appointed section from config file


def delete_section(filename, del_section):
    config = ConfigParser.ConfigParser()
    config.read(filename)
    res = config.remove_section(del_section)
    if res:
        config.write(open(filename, 'w'))

    return res

# update section for list


def update_section(filename, section, option, values):
    config = ConfigParser.ConfigParser()
    config.read(filename)
    subnets = config.get(section, option)
    subs = json.loads(subnets) + values
    config.set(section, option, json.dumps(subs))
    config.write(open(filename, 'w'))

# 更新option的值


def update_option(filename, section, option, value):
    config = ConfigParser.ConfigParser()
    config.read(filename)
    config.set(section, option, value)
    write_config(filename, config)

# check section from config file


def check_section(filename, section):
    config = ConfigParser.ConfigParser()
    config.read(filename)
    if section in config.sections():
        return True
    else:
        return False

if __name__ == "__main__":
    data = {'path': {
        'cf_defalt_path': '',
        'cf_defalt': ''},
        'displayjson': {
        'colour': '',
        'indent': ''}}
    #create_configfile('config.txt', data)
    print update_option('config.txt', 'path', 'cf_defalt_path', 'd://')
