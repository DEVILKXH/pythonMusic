# -*- coding: UTF-8 -*-
# -*- author: kexiaohong -*-

from pythonMusic.utils import  UUIDUtil


#   使用过的url类
class MusicUrlUsed(object):
    __uuid__ = None
    __music_url_used__ = None


def getuuid():
    if MusicUrlUsed.__uuid__ is None:
        MusicUrlUsed.__uuid__ = UUIDUtil.getuuid()
    return MusicUrlUsed.__uuid__

def getmusicurlused():
    if MusicUrlUsed.__music_url_used__ is None:
        MusicUrlUsed.__music_url_used__ = ""
    return MusicUrlUsed.__music_url_used__


def setmusicurlused(musicUrlUsed):
    MusicUrlUsed.__music_url_used__ = musicUrlUsed


def clear():
    MusicUrlUsed.__uuid__ = None
    MusicUrlUsed.__music_url_used__ = None


def tostring():
    return {
        "uuid": getuuid(),
        "music_url_used": getmusicurlused()
    }