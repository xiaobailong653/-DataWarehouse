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
