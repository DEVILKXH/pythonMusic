# -*- coding: UTF-8 -*-
# -*- author: kexiaohong -*-
from pythonMusic.properties import  const


#   URL信息常量分类
class BaseUrl(object):
    __url__ = ""
    __baseurl__ = ""
    __hosturl__ = ""
    __connect__ = ""

    __baidu__ = {
        "url" : "baidu",
        "baseurl" : "http://music.baidu.com",
        "hosturl" : "baidu.com",
        "connect": "http://music.baidu.com"
    }

    __baiduTag__ = {
        "url": "baidu",
        "baseurl": "http://music.baidu.com/",
        "hosturl": "baidu.com",
        "connect": "http://music.baidu.com/tag"
    }

    def __setbaseurl__(self,urls):
        BaseUrl.__url__ = urls['url']
        BaseUrl.__baseurl__ = urls['baseurl']
        BaseUrl.__hosturl__ = urls['hosturl']
        BaseUrl.__connect__ = urls['connect']


def setbaseurls(type):
    switch = {
        const.BAIDU: lambda :BaseUrl().__setbaseurl__(BaseUrl.__baidu__),
        const.BAIFUTAG: lambda :BaseUrl().__setbaseurl__(BaseUrl.__baiduTag__)
    }
    switch[type]()


def getbaseurls():
    base = {
        "url" : BaseUrl.__url__,
        "baseurl": BaseUrl.__baseurl__,
        "hosturl": BaseUrl.__hosturl__,
        "connect": BaseUrl.__connect__
    }
    return base


if __name__ == "__main__":
    setbaseurls(const.BAIDU)
    print getbaseurls()
