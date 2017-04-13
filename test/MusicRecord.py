# -*- coding: UTF-8 -*-
# -*- author: kexiaohong -*-
import UUIDUtil


class MusicRecord(object):

    __uuid__ = None
    __musicName__ = None

def getUuid():
    if(MusicRecord.__uuid__ == None or MusicRecord.__uuid__.strip() == ""):
        MusicRecord.__uuid__ = UUIDUtil.getuuid()
    return MusicRecord.__uuid__


def setMusicName(musicName):
    MusicRecord.__musicName__ = musicName


def getMusicName():
    return MusicRecord.__musicName__


def clear():
    MusicRecord.__uuid__ = None
    MusicRecord.__musicName__ = None