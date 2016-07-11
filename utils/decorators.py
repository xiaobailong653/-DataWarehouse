# -*- coding: utf8 -*-
#################################################
# Create By : sunlf
#
# Create On : 2016-06-29
#
# Comment : DataWarehouse
#################################################


# 延迟初始化装饰器
def lazy_property(cls):
    attr_name = "_lazy_" + cls.__name__

    @property
    def _lazy_property(self):
        if not hasattr(self, attr_name):
            setattr(self, attr_name, cls(self))
        return getattr(self, attr_name)

    return _lazy_property


# 单例模式
def singleton(cls, *args, **kw):
    instances = {}

    def _singleton(*args, **kw):
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]
    return _singleton

'''
@singleton
class Myclass(object):
    def __init__(self, parent):
        self.parent = parent
        self.x = 1
        self.y = 2

obj1 = Myclass("farther")
obj1.x = 4
obj2 = Myclass("marther")
obj2.y = 5
print obj2.x
print obj1.y
'''
