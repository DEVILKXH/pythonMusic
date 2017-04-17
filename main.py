# -*- coding: UTF-8 -*-
# -*- author: kexiaohong -*-
from bs4 import BeautifulSoup

from controller import MusicController
from properties import BaseUrl
from properties import const
from pythonMusic.mapper import UrlMapper

if __name__ == "__main__":
    print const.START
    BaseUrl.setbaseurls(const.BAIDU)
    print BaseUrl.getbaseurls()
    html = UrlMapper.get_content(BaseUrl.getbaseurls()['connect'])
    if html is not None:
        soup = BeautifulSoup(html,'html5lib')
        MusicController.getindexmusic(soup,BaseUrl.getbaseurls())

    BaseUrl.setbaseurls(const.BAIFUTAG)
    print BaseUrl.getbaseurls()
    html = UrlMapper.get_content(BaseUrl.getbaseurls()['connect'])
    if html is not None:
        soup = BeautifulSoup(html, 'html5lib')
        MusicController.gettypemusic(soup, BaseUrl.getbaseurls())

