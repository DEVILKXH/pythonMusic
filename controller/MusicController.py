# -*- coding: UTF-8 -*-
# -*- author: kexiaohong -*-
from pythonMusic.properties import tagattr
from pythonMusic.utils import TagUtils
from pythonMusic.properties import MusicType
from pythonMusic.service import MusicService


class MusicController(object):
    __TYPE__ = ""


def getindexmusic(soup):
    ranklist = TagUtils.gethtmlnodebyclass(soup,tagattr.__DIV__,MusicType.RANKLISTWRAPPER)
    i = 0
    for rankmusic in ranklist:
        MusicService.insertRankList(rankmusic,MusicType.MusicType[i])
        i += 1

def gettypemusic(soup):
    pass