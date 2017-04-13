# -*- coding: UTF-8 -*-
# -*- author: kexiaohong -*-
import urllib2
import urllib
import random


def get_content(url,data = None):
    try:
        timeout = random.choice(range(180,380))
        value = {}
        value['username'] = ''
        value['password'] = ''
        data = urllib.urlencode(value)
        request = urllib2.Request(url=url)
        rep = urllib2.urlopen(request,timeout=timeout)
        return rep.read()
    except :
        print url , " connect error"
        return None

