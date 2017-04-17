# -*- coding: UTF-8 -*-
# -*- author: kexiaohong -*-
from pythonMusic.properties import tagattr
from pythonMusic.utils import TagUtils
from pythonMusic.properties import Music
from pythonMusic.service import MusicService


class MusicController(object):
    __TYPE__ = ""


#   获取首页推荐音乐
def getindexmusic(soup,baseurl):
    ranklist = TagUtils.gethtmlnodebyclass(soup, tagattr.__DIV__, Music.MODSONGRANK)
    i = 0
    for rankmusic in ranklist:
        MusicType = rankmusic.find(class_='title')
        MusicService.insertranklist(rankmusic, TagUtils.gethtmlcontent(MusicType,tagattr.__CONTENT__),baseurl)
        i += 1


#   获取音乐分类
def gettypemusic(soup,baseurl):
    MusicService.gettypemusic(soup,baseurl)


