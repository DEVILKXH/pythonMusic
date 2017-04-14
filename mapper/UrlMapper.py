# -*- coding: UTF-8 -*-
# -*- author: kexiaohong -*-
import urllib2
import urllib
import random
import SQLMapper
from pythonMusic.utils import UUIDUtil


class UrlMapper(object):

    def __getconnection__(self,url,data = None):
        # try:
            timeout = random.choice(range(180, 380))
            value = {}
            value['username'] = ''
            value['password'] = ''
            data = urllib.urlencode(value)
            request = urllib2.Request(url=url)
            rep = urllib2.urlopen(request, timeout=timeout)
            return rep.read()
        # except:
            print url, " connect error"
            return None


#   获取URL页面返回的内容
def get_content(url,data = None):
    return UrlMapper().__getconnection__(url)


#   判断URL是否使用过
def isused(url):
    sql = "select count(0) from music_url_used where music_url = '%s'" % (url)
    result = SQLMapper.getdata(sql)
    count = 0
    for row in result:
        if row[0] == 0:
            return False
    return True

#   插入url
def insert(url,table):
    sql = "insert into %s(uuid,music_url) values('%s','%s')" % (table,UUIDUtil.getuuid(),url)
    print sql
    SQLMapper.insert(sql)