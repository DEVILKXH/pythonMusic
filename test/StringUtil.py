# -*- coding: UTF-8 -*-
# -*- author: kexiaohong -*-
import re


class StringUtil(object):

    def __init__(self):
        print "----StringUtil----"

    def __replace__(self,string,old,new):
        return str(string).replace(old,new)


def replace(string,old,new):
    stringUtil = StringUtil()
    return stringUtil.__replace__(string,old,new)
