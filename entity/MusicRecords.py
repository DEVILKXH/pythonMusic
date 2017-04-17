# -*- coding: UTF-8 -*-
# -*- author: kexiaohong -*-
#!/pythonMusic

from pythonMusic.utils import UUIDUtil
from pythonMusic.properties import BaseUrl


#   音乐记录类
#   extends  object
class MusicRecords(object):
    #   uuid
    __uuid__ = None
    #   名称
    __musicName__ = None
    #   歌手
    __musicSinger__ = None
    #   专辑
    __musicAlbum__ = None
    #   描述
    __musicDesc__ = None
    #   在线地址
    __musicOnLine__ = None
    #   下载地址
    __musicDownLoad__ = None
    #   音乐分类
    __musicType__ = None
    #   音乐来源
    __musicSource__ = None


def getmusicname():
    if(MusicRecords.__musicName__ is None):
        MusicRecords.__musicName__ = ''
    return MusicRecords.__musicName__


def setmusicname(musicNmae):
    MusicRecords.__musicName__ = musicNmae


def getuuid():
    if(MusicRecords.__uuid__ is None):
        MusicRecords.__uuid__ = UUIDUtil.getuuid()
    return MusicRecords.__uuid__


def getmusicsinger():
    if MusicRecords.__musicSinger__ is None:
        MusicRecords.__musicSinger__ = ""
    return MusicRecords.__musicSinger__


def setmusicsinger(musicSinger):
    MusicRecords.__musicSinger__ = musicSinger


def getmusicalbum():
    if MusicRecords.__musicAlbum__ is None:
        MusicRecords.__musicAlbum__ = ""
    return MusicRecords.__musicAlbum__


def setmusicalbum(musicAlbum):
    MusicRecords.__musicAlbum__ = musicAlbum


def getmusicdesc():
    if MusicRecords.__musicDesc__ is None:
        MusicRecords.__musicDesc__ = ""
    return MusicRecords.__musicDesc__


def setmusicdesc(musicDesc):
    MusicRecords.__musicDesc__ = musicDesc


def getmusiconline():
    if MusicRecords.__musicOnLine__ is None:
        MusicRecords.__musicOnLine__ = ""
    return MusicRecords.__musicOnLine__


def setmusiconline(musicOnline):
    MusicRecords.__musicOnLine__ = musicOnline


def getmusicdownload():
    if MusicRecords.__musicDownLoad__ is None:
        MusicRecords.__musicDownLoad__ = ""
    return MusicRecords.__musicDownLoad__


def setmusicdownload(musicDownload):
    MusicRecords.__musicDownLoad__ = musicDownload


def getmusictype():
    if MusicRecords.__musicType__ is None:
        MusicRecords.__musicType__ = ""
    return MusicRecords.__musicType__


def setmusictype(musicType):
    MusicRecords.__musicType__ = musicType


def getmusicsource():
    if MusicRecords.__musicSource__ is None:
        MusicRecords.__musicSource__ = BaseUrl.getbaseurls()['url']
    return MusicRecords.__musicSource__


def setmusicsource(musicSource):
    MusicRecords.__musicSource__ = musicSource


def clear():
    MusicRecords.__uuid__ = None
    MusicRecords.__musicName__ = None
    MusicRecords.__musicSinger__ = None
    MusicRecords.__musicAlbum__ = None
    MusicRecords.__musicDesc__ = None
    MusicRecords.__musicOnLine__ = None
    MusicRecords. __musicDownLoad__ = None
    MusicRecords. __musicType__ = None
    MusicRecords.__musicSource__ = None


def tostring():
    return {
        "uuid": getuuid(),
        "music_name": getmusicname(),
        "music_singer": getmusicsinger(),
        "music_album": getmusicalbum(),
        "music_desc": getmusicdesc(),
        "music_url_online": getmusiconline(),
        "music_url_download": getmusicdownload(),
        "music_type": getmusictype(),
        "music_source": getmusicsource()
    }