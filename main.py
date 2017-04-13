# -*- coding: UTF-8 -*-
# -*- author: kexiaohong -*-
from bs4 import BeautifulSoup

from controller import MusicController
from properties import baseurls
from properties import const
from pythonMusic.mapper import UrlMapper

if __name__ == "__min__":
    print const.START
    baseurls.baseurl = baseurls.baidubaseurl
    baseurls.hosturl = baseurls.baiduhosturl
    baseurls.url = baseurls.baiduurl
    html = UrlMapper.get_content(baseurls.baiduurl)
    if html is not None:
        soup = BeautifulSoup(html,'html5lib')
        MusicController.getindexmusic(soup)
        MusicController.gettypemusic(soup)

