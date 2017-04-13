# -*- coding: UTF-8 -*-
# -*- author: kexiaohong -*-


#   字符串操作工具类
class StringUtil(object):
    def __init__(self):
        pass

    def __replace__(self,string,old,new):
        return str(string).replace(old,new)

#   字符串替换
def replace(string,old,new):
    stringUtil = StringUtil()
    return stringUtil.__replace__(string,old,new)