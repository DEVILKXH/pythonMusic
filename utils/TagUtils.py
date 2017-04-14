# -*- coding: UTF-8 -*-
# -*- author: kexiaohong -*-
import re
from pythonMusic.properties import const
from pythonMusic.properties import tagattr
from pythonMusic.properties import BaseUrl


#   html标签工具类
class TagUtils(object):
    def __init__(self):
        pass
    #   获取标签的title内容
    def __gettagtitle__(self, tag):
        if tag.has_attr(tagattr.__TITLE__) and tag[tagattr.__TITLE__] is not None:
            return tag[tagattr.__TITLE__].strip()
        else:
            return self.__getTagContent__(tag)

    # 获取标签href的内容
    def __gettaghref__(self, tag):
        if tag.has_attr(tagattr.__HREF__) and tag[tagattr.__HREF__] is not None:
            print BaseUrl.getbaseurls()
            if tag[tagattr.__HREF__].find(BaseUrl.getbaseurls()['url'], 0, 20) == -1:
                return BaseUrl.getbaseurls()['baseurl'] + "/" + tag[tagattr.__HREF__].strip()
            else:
                return tag[tagattr.__HREF__].strip()
        else:
            return None

    # 获取标签的内容
    def __gettagcontent__(self, tag):
        if tag is not None :
            return re.sub("<[^<>]+>", "", str(tag)).strip()
        else:
            return const.NULL

    # 获取标签其他任意属性名称
    def __gettagattr__(self, tag, attr):
        if tag.has_attr(attr) and tag[attr] is not None:
            return tag[attr].strip()
        else:
            return const.NULL

    # 获取标签属性，模仿switch-case语句
    def __gethtmlcontent__(self, tag, attr):
        if tag is None:
            return None
        try:
            switch = {
                tagattr.__TITLE__: lambda: self.__gettagtitle__(tag),
                tagattr.__HREF__: lambda: self.__gettaghref__(tag),
                tagattr.__CONTENT__: lambda: self.__gettagcontent__(tag)
            }
            return switch[attr]()
        except:
            return self.__gettagattr__(tag, attr)

    # 根据标签的类名获取节点
    def __getnodebyclass__(self,soup,tag,classname):
        return soup.find_all(tag,class_=classname)


#   获取标签属性内容
def gethtmlcontent(tag, attr):
    tagUtils = TagUtils()
    return tagUtils.__gethtmlcontent__(tag, attr)


#   根据标签的类名获取节点
def gethtmlnodebyclass(soup,tag,classname):
    return TagUtils().__getnodebyclass__(soup,tag,classname)