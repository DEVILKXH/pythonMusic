# -*- coding: UTF-8 -*-
# -*- author: kexiaohong -*-

from pythonMusic.utils import UUIDUtil


#   未使用过的url
class MusicUrlUnuse(object):
    __uuid__ = None
    __music_url__ = None


def getuuid():
    if (musicUrlUnuse.__uuid__ is None):
        musicUrlUnuse.__uuid__ = UUIDUtil.getuuid()
    return musicUrlUnuse.__uuid__


def getmusicurl():
    if MusicUrlUnuse.__music_url__ is None:
        MusicUrlUnuse.__music_url__ = ""
    return MusicUrlUnuse.__music_url__


def setmusicurl(musicUrl):
    MusicUrlUnuse.__uuid__ = musicUrl


def clear():
    MusicUrlUnuse.__uuid__ = None
    MusicUrlUnuse.__music_url__ = None


def tostring():
    return {
        "uuid": getuuid(),
        "music_url": getmusicurl()
    }